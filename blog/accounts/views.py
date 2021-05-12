from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegister
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import AccountUpdateForm
import time



# Using function based view all throughout
def signup_view(request):
    template_name = "accounts/signup.html"
    if request.method == 'POST':
        signup_form = UserRegister(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.save()
            time.sleep(2)
            messages.success(request, f" Your account has successfully been created, you can now log in".capitalize())
            time.sleep(2)
            return redirect('account-login')
        else:
            messages.error(request, f" Some of your information are either existing or not matching, try again")
            return redirect('account-signup')
    else:
        template_name = "accounts/signup.html"
    signup_form = UserRegister()
    context = {"signup_form":signup_form}
    return render(request, template_name, context)


def login_view(request):
    template_name = "accounts/login.html"
    if request.method == "POST":
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            messages.success(request, f"welcome {user}, you are now logged in".capitalize())
            time.sleep(3)
            login(request, user)
            return redirect("post-list")
        else:
            messages.error(request, f"Invalid Username or password")
            return redirect('account-login')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('post-list')
    else:
        template_name = "accounts/login.html"
    login_form = AuthenticationForm()
    context = {"login_form":login_form}
    return render(request, template_name, context)


@login_required(login_url='account-login')
def profile_view(request):    
    if request.method == 'POST':
        a_update = AccountUpdateForm(data=request.POST, instance=request.user)
        if a_update.is_valid():
            a_update.save()
            messages.success(request, "your account has been updated".capitalize())
            return redirect('account-profile')
    else:
        a_update = AccountUpdateForm(instance=request.user)
    template_name = 'accounts/user_profile.html'
    content = { 
        "a_update": a_update,
    }
    return render(request, template_name, content)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        template = "accounts/logout.html"
        return render(request, template)
    