from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.template import loader


# Create your views here.
def main(request):
    return HttpResponse('Welcome')

# def login(request):
#     template = loader.get_template('login.html')
#     return HttpResponse(template.render())

def home(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('/home')
        else:
            messages.error(request, "Registration failed")
    else:
        form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})
