from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }
        error_messages = {
            'username': {
                'required': 'Username is required.',
                'invalid': 'This value may contain only letters, numbers, and @/./+/-/_ characters.',
            },
            'email': {
                'required': 'Email is required.',
                'invalid': 'Enter a valid email address.',
            },
            'password1': {
                'required': 'Password is required.',
            },
            'password2': {
                'required': 'Please confirm your password.',
            },
        }

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',  'image', 'description']
