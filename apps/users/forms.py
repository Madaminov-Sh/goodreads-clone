from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('email already exists')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) <= 8:
            raise ValidationError("password 8 ta belgidan kam bo'lmasligi kerak")
        elif password.isdigit():
            raise ValidationError("password faqat raqamlar ketmaketligidan iborat bo'lmasligi kerak")
        return password

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 5:
            raise ValidationError("username 5 ta belgidan kam bo'lmasligi kerak")
        elif username[0].isdigit():
            raise ValidationError("username'ning birinchi belgisi raqam bo'lmasligi kerak")
        return username

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('username hato')

        if not User.objects.filter(password=password).exists():
            raise forms.ValidationError('password hato')

        return self.cleaned_data



