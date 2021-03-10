from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib import messages


class CustomUserCreationForm(UserCreationForm):
    def clean_email(self):
        demail = self.cleaned_data['email']
        if "amrita.edu" not in demail:
            raise forms.ValidationError("You must be use collage Email ID")
            message = "You already Booked the Room One can Book Only one Room"
            messages.error(request, message)
            return redirect('register_page')
        return demail

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class settigs_form(ModelForm):
    DOB = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    class Meta:
        model = CustomUser
        fields = ['email','name','Gender','DOB','phone_number','profile_pic','address1','address2','pin_code','city','country','proof']
