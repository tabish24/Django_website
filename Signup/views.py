from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from Signup.models import Members

def index(request):
    
    
    
    template = loader.get_template('Signup.html')
    return HttpResponse(template.render())

def signupdata(request):
    print("signupdata")
    print(request.GET)
    print(request.GET['fname'])


    en=Members(
    fname=request.GET['fname'],
    lname=request.GET['lname'],
    dob=request.GET['dob'], 
    gender=request.GET['gender'],
    phoneno=request.GET['phoneno'], 
    email=request.GET['email'],
    password=request.GET['password'],
    comfirmpassword=request.GET['confirmpassword']
    )
    en.save()
    


    str1="Signup successfull: Please login now." + str(en.fname) 
    return render(request,'Signup.html',{'msg':str1})
    
