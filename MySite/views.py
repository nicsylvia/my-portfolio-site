from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from MySite.models import *

# Create your views here.

def Home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        submit_data = Message(name=name, email=email, subject=subject, contact=contact)
        submit_data.save()
        if submit_data:
            messages.success(request, 'Your message has been sent. Thank you!')
        else:
            messages.error(request, 'an error occured, try again')


    blog = Blog.objects.all()
    return render(request, 'public/frontend/index.html', {'blog':blog})

