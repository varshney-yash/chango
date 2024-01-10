from django.shortcuts import render
from .models import Space
from django.contrib.auth.decorators import login_required

@login_required
def spaces(request):
    spaces = Space.objects.all()
    return render(request,'space/spaces.html',{'spaces':spaces})
