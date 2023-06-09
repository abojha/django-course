from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        # CHECK USERS CREDENTIALS IS VALID OR NOT
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')