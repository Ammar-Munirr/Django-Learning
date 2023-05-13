from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello Ammar</h1>')



def home(request):
    return HttpResponse("<h2>Welcome Home</h2>")


def tempelate(request):
    return render(request,'index.html')