from django.shortcuts import redirect, render
from django.views import View

from apps.users.forms import RegisterForm


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
