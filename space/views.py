from django.shortcuts import render
from .models import Space, Message
from django.contrib.auth.decorators import login_required

@login_required
def spaces(request):
    spaces = Space.objects.all()
    return render(request,'space/spaces.html',{'spaces':spaces})

@login_required
def space(request, slug):
    space = Space.objects.get(slug=slug)
    messages = Message.objects.filter(space=space)[:30]
    return render(request, 'space/space_detail.html',{'space':space,'messages':messages})
