from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from Signup.models import Members

def index(request):
    
    
    
    template = loader.get_template('Login.html')
    return HttpResponse(template.render())

def login(request):
    print("login")
    print(request.GET)
    if Members.objects.filter(username=request.GET['username']).exists() and Members.objects.filter(pwd=request.GET['password']).exists():
        str="Successfully Login"
        
    else:
        str="Incorrect username & password"
    


    print(str)
    
    
    return render(request,'login.html',{'msg':str})


