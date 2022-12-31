from django.template import loader
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import requests
from Signup.models import Members
from django.contrib import messages

from django.conf import settings


from django.core.mail import send_mail



def index(request):
    
    
     return render(request,'Signup.html')
    # template = loader.get_template('Signup.html')
    # return HttpResponse(template.render())

def signupdata(request):
    print(request)
    # if request.method == "POST":
    en=Members(
    fname =request.POST.get('fname',""),
    lname=request.POST.get('lname',""),
    dob=request.POST.get('dob',""),
    gender=request.POST.get('gender',""),
    phone=request.POST.get('phone',123),
    email=request.POST.get('email',""),
    password=request.POST.get('password',""),
    cpassword=request.POST.get('cpassword',""))
    en.save()
    messages.success(request, "Yor details submitted successfully")

    print("signupdata")
    # print(request.GET)
    # print(request.GET['fname'])

    subject = 'Thank you for registering .'
    message = f'please verify the email by click the link (link) .'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [ request.POST.get('email',"")]
    

    send_mail( subject, message, email_from, recipient_list )
    

    str1="Signup successfull: Please verify link by Email" + str(en.fname) 
    return render(request,'Signup.html',{'msg':str1})


    # en=Members(firstname=request.POST['fname'],
    # lastname=request.POST['lname'],
    # dob=request.POST['dob'],
    # gender=request.POST['gender'],
    # phoneno=request.POST['phoneno'],
    # email=request.POST['email'],
    # password=request.POST['password'],
    # comfirm_password=request.POST['confirm_password'])
    # en.save()
    


    # str1="Signup successfull: Please login now." + str(en.id) 
    # return render(request,'Signup.html',{'msg':str1})
     