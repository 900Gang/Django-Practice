from django.urls import path,include
from . import views


#Template URLS

app_name='user_app'

urlpatterns=[
    path('register/$',views.register,name='register')
]