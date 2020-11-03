'''
from django.shortcuts import render
from .models import Course

def example(request):
    plant = request.session.get('plant')
    querydata = Course.get_db(plant).objects.all()
    return render(request, 'example.html', {'querydata': querydata})
'''
