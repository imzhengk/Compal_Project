# Requirements

 - Python 3.5
 - Django 2.2

# Installation
Install using `pip`...

    pip install django-myplant

Add `'myplant'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = [
        ...
        'myplant',
    ]
    
# Example

Add json such as below to `setting.py`.

    PLANT = {
        'plant1' : 'Plant1',
        'cd' : 'CD',
    }
    # the key is requested parameter,the value is class name prefix
