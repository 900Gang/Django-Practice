"""
URL configuration for second_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from second_app import views,forms

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^help/',include('second_app.urls')),
    re_path(r'^acc_table/$',views.acc_table,name='acc_table'),
    re_path(r'^use/$',views.use,name='use'),
    re_path(r'^form/$',views.form_name_view,name='form_name_view'),
    path('admin/', admin.site.urls),
    
]
