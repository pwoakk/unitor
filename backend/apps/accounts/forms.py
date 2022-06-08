from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'autocomplete': 'off',
            'placeholder': 'Введите пароль'
        })
    )


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Введите пароль'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Введите пароль'
        })
    )

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'date_birth',
            'gender',
            'phone',
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'gender': forms.ChoiceField(),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
