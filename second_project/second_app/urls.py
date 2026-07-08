from django.urls import path,re_path
from second_app import views
from . import forms

urlpatterns = [
    re_path(r'^$',views.help_app,name='help_app'),
    re_path(r'^acc_table/$',views.acc_table,name='acc_table'),
    re_path(r'^use/$',views.use,name='use'),
    re_path(r'^form/$',views.form_name_view,name='form_name_view'),

]