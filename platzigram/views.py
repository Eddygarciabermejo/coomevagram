""" Platzigram views module """

import pdb
import json

from django.http import HttpResponse, JsonResponse
from datetime import datetime


def current_server_time(request):
    """
    Return current server time.
    :param: request
    :return: String with a message.
    """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))


def order_numbers(request):
    """
    Return a JSON response with sorted integer.
    :param: request
    :return: json

    http://localhost:8000/order-numbers/?numbers=5,4,1
    {"order_numbers": [1, 4, 5]}
    """

    # Define un Debug en consola al momento de realizar la petición.
    # pdb.set_trace()

    # Forma 1
    numbers_order = map(lambda x: int(x), request.GET['numbers'].split(','))
    # Forma 2
    # numbers_order = [int(i) for i in request.GET['numbers'].split(',')]

    data = {
        'status': 'ok',
        'numbers': sorted(numbers_order),
        'message': 'Integers sorted successfully.'
    }

    # Forma 1
    # return JsonResponse(data=data, safe=False)
    # Forma 2
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    """
    Return a welcome message or block.
    Envía parámetros posicionales según el tipo definido en la url.
    :param request:
    :param name:
    :param age:
    :return:

    http://localhost:8000/hi/Yesica/11/
    """

    if age < 12:
        message = 'Sorry {}, you are not allowed here!'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram!'.format(name)

    return HttpResponse(message)
