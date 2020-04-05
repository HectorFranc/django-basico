"""Platzigram views"""
#  Django
from django.http import HttpResponse

#  Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hi! The current hour is {now}')


def sort_integers(request):
    """Json response with sorted integers"""
    numbers = request.GET['numbers'].split(',')
    numbers = map(lambda number: int(number), numbers)
    numbers = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = f'Sorry {name}, you are not allowed to be here'
    else:
        message = f'Hi {name}!\nWelcome to Platzigram'

    return HttpResponse(message)
