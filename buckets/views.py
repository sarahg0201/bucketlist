from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def index(request):
    buckets = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.info(request, "You must input a valid URL.")
        return redirect('/')

    context = {'buckets':buckets, 'form':form}
    return render(request, 'buckets/list.html', context)

def editBucket(request, pk):
    bucket = Task.objects.get(id=pk)

    form = TaskForm(instance = bucket)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance = bucket)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'buckets/edit_bucket.html', context)

def deleteBucket(request, pk):
    item = Task.objects.get(id = pk)

    if request.method == 'POST': 
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'buckets/confirmDel.html', context)
