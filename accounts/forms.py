from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Customer
from accounts.utils import old_enough


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'style': 'width:316px',
        'placeholder': 'Confirm Password',
    }))

    YEARS_CHOICES = [year for year in range(1920, 2007)]

    birth_date = forms.DateField(widget=forms.DateInput(attrs={
        'id': 'datepicker',
        'placeholder': 'Date of Birth'
    }))

    # Make sure username is not already taken.
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username is already taken. Select another username.')
        if len(username) < 5:
            raise forms.ValidationError('Username must be at least 5 characters long.')
        return username

    # Verify if user is at least 21 years old.
    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        is_old_enough = old_enough(birth_date)
        if not is_old_enough:
            raise forms.ValidationError('You must be at least 21 years old to register.')
        return birth_date

   # Make sure email doesn't already exist.
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already taken.')
        return email

    # Make sure password is at least 8 characters long.
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password

    # Password verification
    def clean(self):
        form = self.cleaned_data
        if form['password'] != form['confirm_password']:
            # Raises error message.
            self._errors['password'] = ['Passwords do not match.']
            del form['password']
        return form

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )
        widgets = {
            'username': forms.TextInput(attrs={'style': 'width:316px', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'style': 'width:316px', 'placeholder': 'Email address'}),
            'password': forms.PasswordInput(attrs={'style': 'width:316px', 'placeholder': 'Password'}),
        }
