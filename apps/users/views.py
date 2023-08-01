from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from apps.users.forms import RegisterForm, LoginForm


class RegisterView(View):

    def post(self, request):
        create_form = RegisterForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('/')
        else:
            context = {
                'form': create_form
            }
        return render(request, 'register/register.html', context)

    def get(self, request):
        create_form = RegisterForm()
        context = {
            'form': create_form
        }
        return render(request, 'register/register.html', context)


class LoginView(View):
    def post(self, request):
        form = LoginForm(data=request.POST)
        user = request.user
        if form.is_valid():
            login(request, user)
            messages.success(request, 'muvaffaqiyatli login qilindi')
            return redirect('books:home')
        return render(request, 'register/login.html', {"form": form})


    def get(self, request):
        form = LoginForm()
        return render(request, 'register/login.html', {"form": form})

