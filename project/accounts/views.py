from django.shortcuts import render, redirect
from .forms import EditForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login
from accounts.models import Doctor
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404 
import random
from django.http import Http404  
# Create your views here.


ran1=random.random()
ran2=str(ran1)
rans=ran2.split('.')
num=rans[1]
def profile(request):
    return render(request,'accounts/profile.html',{"rand":num})


@login_required
def edit_prof(request,slug):
    if not slug == num:
        raise Http404  
    else:
        form=EditForm()
        if request.method=='POST':
            form=EditForm(request.POST,request.FILES)
            if form.is_valid():
                new=form.save(commit=False)
                new.user=request.user
                new.save()
                return redirect('/')
        else:
            form = EditForm()
    return render(request,'accounts/e-prof.html',{'form':form,"rand":num})



@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile/')
    else:
        form=SignupForm()
    return render(request,'registration/signup.html',{'form':form})

def ed(request):
    doc=get_object_or_404(Doctor , user=request.user)
    if request.method == 'POST':
        form = EditForm(request.POST,request.FILES,instance=doc)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=EditForm(instance=doc)
        #eform=form.instance
    return render(request,'accounts/ed.html',{'form':form})

