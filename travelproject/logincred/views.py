from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "mail id already taken")
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname,
                                                email=email, password=password)
                user.save();
                print("USER CREATED")
                return redirect('login')

        else:
            messages.info(request, "Password not matched")

    return render(request, "registration.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
