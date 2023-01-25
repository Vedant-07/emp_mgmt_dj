from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    """ print('challo lets begin')
    tim=datetime.datetime.now()
    print(f'the date time is {tim}')
    return HttpResponse("<h1>wazzzzuuuup  </h1>") """
    return render(request,'home.html')

