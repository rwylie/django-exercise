"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import homepage.views
import blog.views
import poll.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage.views.homepage, name='homepage'),
    url(r'^about$', homepage.views.about, name='about'),
    url(r'^hello$', homepage.views.hello, name='hello'),
    url(r'^contact$', homepage.views.contact, name='contact'),
    url(r'^thanks$', homepage.views.thanks, name='thanks'),
    url(r'^blog/(\S+)/(\S+)/$', blog.views.blog_post, name='posts'),
    url(r'^blog/(\S+)/$', blog.views.blog_index, name='blog'),
    url(r'^my_poll/(\S+)$', poll.views.my_poll),
    url(r'^results$', poll.views.results, name='results'),
    url(r'^poll_list$', poll.views.poll_list),
]
