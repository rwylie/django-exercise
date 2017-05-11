from django.template.response import TemplateResponse
from django.core.mail import send_mail
from django import http
import forms


import datetime


def homepage (request):
    context = {
    'page_title': 'HOME PAGE'
    }
    return TemplateResponse(request, 'homepage.html', context)

def about (request):
    context = {
    'page_title': "ABOUT"
    }
    return TemplateResponse(request, 'about.html', context)

def hello (request):
    your_name = request.POST.get('your_name', "Default Name")
    context = {
    'your_name' : your_name
    }
    return TemplateResponse(request, 'hello.html', context)

def contact (request):
    contact_form  = forms.ContactMeForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            send_mail(
                contact_form.cleaned_data['name'],
                contact_form.cleaned_data['email'],
                'ronda@rondawylie.com',
                ['ronda@rondawylie.com'],
                fail_silently=False,
            )
            return http.HttpResponseRedirect('/thanks')
    context = {'form': contact_form}
    return TemplateResponse(request, 'contact.html', context)

def thanks (request):
    context = {}
    return TemplateResponse(request, 'thanks.html', context)
