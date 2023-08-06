from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from apps.users.forms import RegisterForm, LoginForm, UserProfileForm


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
        return render(request, 'users/register/register.html', context)

    def get(self, request):
        create_form = RegisterForm()
        context = {
            'form': create_form
        }
        return render(request, 'users/register/register.html', context)


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
        return render(request, 'users/register/login.html', {'form': form})

    def get(self, request):
        form = LoginForm()
        print('get method')
        return render(request, 'users/register/login.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html', {'user': request.user})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return render(request, 'users/register/logout.html', context={})


class ProfileUpdateView(LoginRequiredMixin, View):
    def post(self, request):
        user_profile_form = UserProfileForm(instance=request.user, data=request.POST)
        if user_profile_form.is_valid():
            user_profile_form.save()
            messages.success(request, 'muvaffaqiyatli o\'zgartirildi')
            return redirect("users:profile")
        return render(request, 'users/profile_update.html', {'form': user_profile_form})
    
    def get(self, request):
        user_profile_form = UserProfileForm(instance=request.user)
        return render(request, 'users/profile_update.html', {'form': user_profile_form})
