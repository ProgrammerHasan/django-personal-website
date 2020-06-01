from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home/index.html')
def profile(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        comments = request.POST.get("comments")
        send_mail('Web@ProgrammerHasan.Info',
        'Subject:'+subject +', Email:'+email +', Name:'+name +', Message:'+comments,
        'mail@programmerhasan.info',
        ['info.msitxpress@gmail.com'],
        fail_silently=False)
        messages.success(request, 'Your Message Send successfully!')
    return render(request,'home/profile.html')
