"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import patterns, url
from .views import IndexView
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'^author_new/', views.author_new, name='author_new'),
    url(r'^author_edit/(?P<pk>\d+)/$', views.author_edit, name='author_edit'),
    url(r'^author_delete/(?P<pk>\d+)/$', views.author_delete, name='author_delete'),
    url(r'^book_new/', views.book_new, name='book_new'),
    url(r'^genre_new/', views.genre_new, name='genre_new'),
    url(r'^book_edit/(?P<pk>\d+)/$', views.book_edit, name='book_edit'),
    url(r'^genre_edit/(?P<pk>\d+)/$', views.genre_edit, name='genre_edit'),
]
