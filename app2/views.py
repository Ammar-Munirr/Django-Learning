from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('Hello')



def home(request):
    return HttpResponse('Welcom Home')


def template(request):
    return render(request,'index.html')