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
            raise ValidationError("password must not be less than 8 characters")
        elif password.isdigit():
            raise ValidationError("the password should not consist of only a sequence of numbers")
        return password

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 5:
            raise ValidationError("username must not be less than 5 characters")
        elif username[0].isdigit():
            raise ValidationError("The first character of username must not be a number")
        return username

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 5:
            raise ValidationError("username must not be less than 5 characters")
        elif username[0].isdigit():
            raise ValidationError("+The first character of username must not be a number")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('email already exists')
        return email