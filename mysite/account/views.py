from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import AccountAuthenticationForm, RegistrationForm 
from django.contrib.auth import authenticate , login , logout



def home(request):
    return render(request, 'account/home.html', {'name':'rabinweb'})






def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('account:home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            print('form', form.cleaned_data)
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            if user:
                login(request, user)
                return redirect('account:home')
    else:
        form = AccountAuthenticationForm()
    
    context['login_form'] = form

    return render(request, 'account/login.html', context)


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)  # احراز هویت کاربر
            if user:
                login(request, user)  # ورود کاربر
                destination = request.GET.get('next')  # دریافت مقدار next از پارامترهای URL
                if destination:
                    return redirect(destination)
                return redirect("account:home")
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)
