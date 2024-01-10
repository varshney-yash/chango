from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request,'account/signup.html',{'form':form})