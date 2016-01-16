from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.shortcuts import render, redirect

from blog.forms import UserLoginForm, RegisterForm
from blog.models import UserInfo

def login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!'
            }
            return render(request, 'login.html', context)

        else:
            login(request, user)
            return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('login')


class RegisterCreateView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
#    success_url = ''
            

