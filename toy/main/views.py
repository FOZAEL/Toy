import re
from django.shortcuts import render
from django.http import HttpResponse
from urllib import response
import requests
from .forms import MyForm

# Create your views here.
def index(request):
    name = 'World!'
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            response = requests.get("http://flask:5000" + "/hello/"+name)
            print(response.json())
            print(response.json()['massage'])
            return render(request, 'index.html',{'form' : form, 'massage' : response.json()["massage"]})
    else:
        form = MyForm()
        return render(request, 'index.html',{'form' : form, 'name' : name})

