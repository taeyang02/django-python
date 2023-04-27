from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('hello')


def first_page(request):
    return HttpResponse('it is ur first page hehe')
