from django.http import HttpResponse
from django.shortcuts import render

import inspect

def index(request):
    return HttpResponse(
        'Hello from {}#{}'.format(__name__, inspect.stack()[0][3])
    )
