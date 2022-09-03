from django import forms
from .models import *

class otpForm(forms.ModelForm):
    class Meta:
        model=otp
        fields=["username",'otps']
