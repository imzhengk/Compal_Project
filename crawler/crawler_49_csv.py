import requests
import csv
import io 
import json

PLANT = {
    '3' : 'KS-P3',
    '2' : 'KS-P2',
    '4' : 'KS-P4',
    '5' : 'KS-P5',
    'CD' : 'CD-Plant'
}

server_url = {
    'KS' : '',
    'CD' : ''
}

def get_baseurl(line):
    base_url = server_url['KS']
    if line.startswith('CD'):
        base_url = server_url['CD']
    return base_url

def get_plantname(line):
    plant_name = ''
    if line.startswith('CD'):
        plant_name = PLANT['CD']
    else:
        plant_name = PLANT[line[0]]
    return plant_name


def get_log_status(date, line):
    base_url = get_baseurl(line)
    plant_name = get_plantname(line)
    url_get_log = base_url + 'get_log_status'
    payload = {
        "date_selected": date,
        "plant_name": plant_name,
        "server_name": line
    }
    r = requests.post(url_get_log, json=payload, timeout=30)
    r.close()
    if r.status_code != 200:
        raise Exception('DailyReport get_log_status fail!')
    return r.json()


def generate_eport(date, line):
    base_url = get_baseurl(line)
    plant_name = get_plantname(line)
    payload = {
        "date_selected": date,
        "plant_name": plant_name,
        "server_name": line
    }
    payload_2 = get_log_status(date, line)
    del payload_2['message']
    del payload_2['output_folder']
    payload_2.update(payload)

    url_sync_log = base_url + 'sync_date_log'

    w = requests.post(url_sync_log, json=payload_2, timeout=30)
    w.close()
    if w.status_code != 200:
        raise Exception('DailyReport sync_date_log fail!')
    payload_3 = w.json()
    del payload_3['message']
    payload_3['date_selected'] = payload['date_selected']
    payload_3['report_task'] = 'ai_aoi'
    url_eport = base_url + 'generate_all_eport'
    e = requests.post(url_eport, json=payload_3)
    e.close()
    if e.status_code != 200:
        raise Exception('DailyReport generate_all_eport fail!')
    win_path = e.json()['report_files']['dir_ai_aoi']
    url_path = '/'.join(win_path.split('\\'))
    return url_path

def get_csv_data(date, line, fast=False):
    base_url = get_baseurl(line)

    if line.startswith('5'):
        line = line[1:]


    report_url = base_url + 'download_report/ai_aoi/'
    path_url = None
    if fast:
        payload_2 = get_log_status(date, line)['report_files']
        if payload_2['stat_ai_aoi']:
            url_path = '/'.join(payload_2['dir_ai_aoi'].split('\\'))
            path_url = report_url + url_path
            print(date + ' ' + line + ' log status is true,so no generate_eport')
        else:
            path_url = report_url + generate_eport(date,line)
    else:
        path_url = report_url + generate_eport(date,line)
    r = requests.get(path_url)
    r.close()
    if r.status_code != 200:
        raise Exception("DailyReport download_report fail!")
    report_csv  = list(csv.reader(io.StringIO(r.text)))
    report_dict = dict(zip(report_csv[0], report_csv[2]))
    return report_dict
