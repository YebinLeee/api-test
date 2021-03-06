"""apiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mapAPI.views as m
import account.views as a

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', m.home, name='home'),
    path('location/', m.location, name='location'),
    path('location/jusoPopup/', m.jusoPopup, name='jusoPopup'),
    path('keyword/', m.keyword, name='keyword'),
    path('category/', m.category, name='category'),
    path('click/', m.clickmarker, name='clickmarker'),
    path('login/', a.login, name='login'),
    path('post_write/', a.post_write, name='post_write'),
    path('post_list/', a.post_list, name='post_list')
]