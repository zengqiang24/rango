from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict={"boldmessage":"this is the bold message for you .please check out!"}
    return render(request,'rango/index.html',context_dict)

def about(request):
    context_dict={"about":"this is qiang blogs"}
    return render(request,'rango/about.html',context_dict)

