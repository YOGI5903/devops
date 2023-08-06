from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Newapp,Todo
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    a=Newapp.objects.all().values()
    t=loader.get_template("index.html")
    context = {"Name":a }
    return HttpResponse(t.render(context,request))
def add(request):
    t=loader.get_template("add.html")
    return HttpResponse(t.render({},request))   
def addrecord(request):
    x=request.POST["first"]
    y=request.POST["last"]
    a=Newapp(firstname=x,lastname=y)
    a.save()
    return HttpResponseRedirect(reverse("index"))
def delete(request,id):
    a=Newapp.objects.get(id=id)
    a.delete()
    return HttpResponseRedirect(reverse("newapp:index"))

def todo(request):
    a=Todo.objects.all().values()
    t=loader.get_template("todo.html")
    context = {"list":a ,"len":len(a)}
    return HttpResponse(t.render(context,request))
def add_list(request):
    x=request.POST["add"]
    a=Todo(work=x)
    a.save()
    return HttpResponseRedirect(reverse("todo"))

def delete_list(request,id):
    a=Todo.objects.get(id=id)
    a.delete()
    return HttpResponseRedirect(reverse("todo"))

def delete_all(request):
    a=Todo.objects.all()
    a.delete()
    return HttpResponseRedirect(reverse("todo"))
