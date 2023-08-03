from django.contrib.auth import login, authenticate
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
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("logined")
                return redirect('books:home')
            else:
                messages.error(request, 'Bunday user mavjud emas')
                redirect('users:register')
        return render(request, 'register/login.html',{'form': form})

    def get(self, request):
        form = LoginForm()
        print('get method')
        return render(request, 'register/login.html',{'form': form})
