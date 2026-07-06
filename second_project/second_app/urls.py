from django.urls import path,re_path
from second_app import views

urlpatterns = [
    re_path(r'^$',views.help_app,name='help_app'),
]