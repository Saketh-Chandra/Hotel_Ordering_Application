from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm,settigs_form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
import re


# Create your views here.

def hello_world(request):
    return render(request,'accounts/home.html')


@unauthenticated_user
def login_views(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('default_home_name')
            # return HttpResponse(f'hello {request.user}')
        else:
            messages.info(request, "username or password is incorrect")
    context = {}
    return render(request, 'accounts/loginPage.html', context)


@unauthenticated_user
def register_views(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save(commit=False)
            user.save()

            user_name = form.cleaned_data.get('username')
            # print(user_name)
            messages.success(request, 'Account was successfully created for ' + user_name)
            return redirect('login_page')
        else:
            messages.error(request, 'Account was unsuccessfully created')
            return redirect('register_page')
    context = {'form': form}
    return render(request, 'accounts/registerPage.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'You are successfully logged out')
    return redirect('login_page')


def default_home(request):
    print('default_home')
    group = None

    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
        print(group)

        if group == 'customer':
            # return redirect('customer_home')
            return redirect('hello')

        elif group == 'manager':
            # return redirect('manager_home')
            return redirect('hello')
        elif group == 'chef':
            # return redirect('chef_home')
            return redirect('hello')

        else:
            message = "You are not authorized to view this page"
            messages.error(request, message)
            return redirect('logout_page')
        # return HttpResponse('You are not authorized to view this page')
    else:
        return redirect('hello')

def settings_view(request):
    userr = request.user
    form = settigs_form(instance=userr)
    if request.method == 'POST':
        form = settigs_form(request.POST,request.FILES,instance=userr)
        if form.is_valid():
            form.save()
            return redirect('hello')
        else:
            return redirect('settings')
    context={'form':form}
    return render(request,'accounts/settings.html',context)