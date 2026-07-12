from django import forms
from django.core import validators
from second_app.models import user




def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("Not Starting With Z")
class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email=forms.EmailField()
    verify_email=forms.EmailField(label="Enter the email again")
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    class Meta:
        model=user
        fields="__all__"

def clean(self):
    all_data_clean=super().clean()
    email=all_data_clean['email']
    vamil=all_data_clean['verify_email']
    if vamil!=email:
        raise forms.ValidationError("Not Matching Emails")

