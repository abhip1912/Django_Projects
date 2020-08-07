from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.conf import settings
import json

# def home(request):
#     return render(request, 'calc/home.html')
def do_nothing(request):
    return render(request, 'calc/home.html')


def home(request):
    # if "number1" in request.POST:
    #     num1 = int(request.POST['number1'])
    #     num2 = int(request.POST['number2'])
    #     s = num1 + num2
    #     result = {
    #         'sum': s
    #     }
    #     return render(request, 'calc/home.html',result)
    # else:
    num1 = int( request.POST.get('n1') )
    num2 = int ( request.POST.get('n2') )
    print(num1, num2)
    result = {
        'sum': num1 + num2,
        'sub': num1 - num2,
        'mul': num1 * num2,
    }
    if num2 == 0:
        div = "Undefined"
    else:
        div = num1 / num2

    result['div'] = div
    return JsonResponse(result)
    # return render(request, 'calc/home.html', {'sum' : s})

@api_view(["POST"])
def apiHome(data):
    yo = json.loads(data.body)
    num1 = yo['n1']
    num2 = yo['n2']
    result = {
        'sum': num1 + num2,
        'sub': num1 - num2,
        'mul': num1 * num2,
    }
    if num2 == 0:
        div = "Undefined"
    else:
        div = num1 / num2

    result['div'] = div
    return JsonResponse(result, safe=False)