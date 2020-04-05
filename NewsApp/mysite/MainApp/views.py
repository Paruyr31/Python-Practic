from django.shortcuts import render
from django.http import *


def hello(request):
    return render(request, 'MainApp/homePage.html')

def contact(request):
    return render(request, 'MainApp/basic.html', {'values': ['Если у вас есть вопросы звоните по номеру',
                                                              '(374) 43 35 38 38',
                                                             'platon-ash@mail.ru']})