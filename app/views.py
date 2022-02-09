from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.core.mail import send_mail,EmailMessage

# Create your views here.
def index(request):
    return render(request,'index.html')


def uploadimage(request):
    print("file Uploading")
    p = request.FILES['image'];
    user = User(pic = p);
    user.save();
    email=EmailMessage('FILE', 'Image_File', 'sharique413@gmail.com', ['Sharique413@gmail.com'])
    email.attach(p.name, p.read(), p.content_type)
    email.send()
    return render(request, 'index.html')