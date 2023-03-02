 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import  CreateUserForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'khudra/index.html')


def register(request): 
        form = CreateUserForm
        if request.method == 'POST':
           form = CreateUserForm(request.POST)
           if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
            #    messages.success(request, 'Account was created for ' + user)
               return redirect('index')
           else:
            print(form.errors)
        context = {'form':form}
        return render(request, 'khudra/register.html', context)

def login_view(request):
    if request.method == "POST":
           username = request.POST.get('username')
           password =request.POST.get('password')
           user = authenticate(request, username=username, password=password)
           if user is not None:
              login(request, user)
              return redirect('index')


           else:
    		       messages.info(request, 'Username OR password is incorrect')

    
    
    return render(request, 'khudra/login.html')