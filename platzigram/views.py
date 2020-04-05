"""Platzigram views"""
#  Django
from django.http import HttpResponse, JsonResponse

#  Utilities
from datetime import datetime


def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hi! The current hour is {now}')


def hi(request):
    """Hi"""
    numbers = request.GET['numbers'].split(',')
    numbers = map(lambda number: int(number), numbers)
    numbers = sorted(numbers)
    return JsonResponse({
        'numbers': numbers
    })
