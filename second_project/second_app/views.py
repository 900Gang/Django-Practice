from django.shortcuts import render
from django.http import HttpResponse 
from second_app.models import AccessRecord,webpage,Topic,user
from . import forms


# Create your views here.
def index(request):
    my_dict = {'insert': "Hello I am from second_app/index.html"}
    return render(request,'second_app/help.html',context=my_dict)
def help_app(request):
    help_dict = {'insert': "HELP!!!!!"}
    return render(request,'second_app/help.html',context=help_dict)

def acc_table(request):
    acc_dict={'access_tab':AccessRecord.objects.order_by('date')}
    return render(request,'second_app/help.html',context=acc_dict)

def use(request):
    user_dict={'user_tab':user.objects.order_by('First_Name')}
    return render(request,'second_app/user.html',context=user_dict)


def form_name_view(request):
    form=forms.FormName()
   

    if request.method=='POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            #Do something code
            print("Validation Success!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
    return render(request,'second_app/forms.html',context={'form': form})