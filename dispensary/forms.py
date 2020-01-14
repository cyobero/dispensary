from django import forms


class ContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    message = forms.CharField(widget=forms.TextInput())
