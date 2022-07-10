from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import task
from .forms import *

# Create your views here.

def index(request):
    tasks=task.objects.all()
    form=TaskForm()

    if request.method=='POST':
        form= TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    content={'tasks':tasks,'form':form}
    return render(request,'tasks/list.html',content)

def updateTask(request,pk):
    tasks = task.objects.get(id=pk)
    form = TaskForm(instance=tasks)

    if request.method=='POST':
        form= TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')

    content={'form':form}
    return render(request,'tasks/update_task.html',content)

def deleteTask(request,pk):
    item=task.objects.get(id=pk)
    content={'item':item}
    if request.method=='POST':
        item.delete()
        return redirect('/')

    return render(request, 'tasks/delete_task.html',content)