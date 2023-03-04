from django.shortcuts import render, HttpResponse
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.views import View
from django.shortcuts import get_object_or_404
from .models import *

#This function will only show all docs

def home(request):
    try:
        doc = Document.objects.all()
        return render(request, 'docs/home.html', {'doc': doc})
    except:
        return render(request, 'docs/home.html')

# User Registration
def signup(request):
    if request.method=='POST':
        fm = UserSignup(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your account has been created Successfully !!!')
    else:
        fm = UserSignup()
    return render(request, 'docs/signup.html', {'form':fm})

def UploadView(request):
    if request.method == 'POST':
        admin_id = request.user.id
        user = User.objects.get(id=admin_id)
        if user.is_superuser == True or user.is_admin == True:
            title = request.POST.get('title')
            docs_file = request.FILES['docs_file']
            description = request.POST.get('description')
            date_posted = request.POST.get('date_posted')
            data = Document(title=title, docs_file=docs_file, description=description, date_posted=date_posted)
            data.save()
            messages.success(request, 'Document uploaded successfully !!!')
            return render(request, 'docs/upload.html')
    return render(request, 'docs/upload.html')

    
def LogoutView(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')

