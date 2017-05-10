from django.template.response import TemplateResponse
from django import forms

import datetime

class NameForm (forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=100)

def homepage (request):
    context = {
    'page_title': 'HOME PAGE'
    }
    return TemplateResponse(request, 'homepage.html', context)

def contact (request):

    context = {
    'page_title': 'CONTACT'
    }
    return TemplateResponse(request, 'contact.html', context)

def about (request):
    context = {
    'page_title': "ABOUT"
    }
    return TemplateResponse(request, 'about.html', context)

def hello (request):
    your_name = request.POST.get('your_name', "Default Name")
    context = {
	"your_name" : your_name
    }
	return TemplateResponse(request, 'hello.html', context)
