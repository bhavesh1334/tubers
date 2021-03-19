from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contuber



def contuber(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        company_name=request.POST['company_name']
        subject=request.POST['subject']
        message = request.POST['message']
        contuber= Contuber(full_name=full_name, email=email, phone=phone, company_name=company_name,subject=subject, message=message)
        contuber.save()
        messages.success(request, 'Thanks for reaching us!')
        return redirect('/')
