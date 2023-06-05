from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contacts
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
       'variables1': "this is sent",
       "variables2": "This is another variable"
    }
    # return HttpResponse('This is Home Page')
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is About Page')

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('This is Services Page')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contacts(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contacts.html')
    # return HttpResponse('This is Contacts Page')