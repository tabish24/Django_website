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


    en=Members(firstname=request.GET['fname'],lastname=request.GET['lname'],username=request.GET['username'],email=request.GET['email'],pwd=request.GET['password'],)
    en.save()
    


    str1="Signup successfull: Please login now." + str(en.id) 
    return render(request,'Signup.html',{'msg':str1})
    
