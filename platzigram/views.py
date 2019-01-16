""" Platzigram views module """

import pdb

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
    Return order numbers.
    :param: request
    :return: json

    http://localhost:8000/order-numbers/?numbers=5,4,1
    ["1", "4", "5"]
    """

    # Define un Debug en consola al momento de realizar la petición.
    # pdb.set_trace()

    numbers = sorted(request.GET['numbers'].split(','))

    return HttpResponse(JsonResponse(numbers, safe=False))
