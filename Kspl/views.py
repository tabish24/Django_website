from django.shortcuts import render, HttpResponse

# Create your views here.
def Kspl(request):
    return HttpResponse("this is a boy view which is created by tabish")

    # def path(request):
    # return HttpResponse("this is a path view which is created by tabish")
def path(request):
    context ={
        'heading ':"django tutorial 1",
        'context':"this is the est djangot utorial on this entire planet"
    }
    return HttpResponse("this is a path view which is created by tabish ")