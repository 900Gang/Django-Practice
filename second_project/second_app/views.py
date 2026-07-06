from django.shortcuts import render
from django.http import HttpResponse    


# Create your views here.
def index(request):
    my_dict = {'insert': "Hello I am from second_app/index.html"}
    return render(request,'second_app/help.html',context=my_dict)
def help_app(request):
    help_dict = {'insert': "HELP!!!!!"}
    return render(request,'second_app/help.html',context=help_dict)