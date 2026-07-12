from django.shortcuts import render
#from django.http import HttpResponse
from .forms import NewUser


# Create your views here.
def index(request):
    return render(request,'first_app/index.html')

def users(request):
    form= NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            raise SyntaxError
    return render(request,'first_app/user.html',{'form':form})