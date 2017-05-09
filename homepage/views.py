from django.template.response import TemplateResponse

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
