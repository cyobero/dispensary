from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Customer


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'style':'width:316px',
        'placeholder': 'Confirm Password',
        }))

    YEARS_CHOICES = [year for year in range(1920, 2015)]

    birth_date = forms.DateField(widget=forms.DateInput(attrs={
        'id': 'datepicker',
        'placeholder': 'Date of Birth'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )
        widgets = {
            'username': forms.TextInput(attrs={'style':'width:316px', 'placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'style':'width:316px', 'placeholder':'Email address'}),
            'password': forms.PasswordInput(attrs={'style':'width:316px', 'placeholder':'Password'}),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', )
