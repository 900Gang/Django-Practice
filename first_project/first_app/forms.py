from django import forms
from django.core import validators
from first_app.models import User


class NewUser(forms.ModelForm):
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label="Enter the email again")
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = User
        fields= '__all__'