from django.core import validators
from enroll.models import User
from django import forms 

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name' , 'email' , 'password']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'forms-control'}),
            'email' : forms.EmailInput(attrs={'class': 'forms-control'}),
            'password' : forms.PasswordInput(render_value=True, attrs={'class' : 'forms-control'})
        }
        