from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ListForm
from .models import List


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            items = List.objects.all
            messages.success(request, "Item Has Been Successfully Added To The List")
            return render(request, 'home.html', {'all_items': items})

    else:
        items = List.objects.all
        return render(request, 'home.html', {'all_items': items})


def about(request):
    context = {'name': 'Ajay Yadav'}
    return render(request, 'about.html', context)


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, "Item Has Been Successfully Deleted")
    return redirect('home')


def cross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.is_completed = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.is_completed = False
    item.save()
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item Has Been Edited!")
            return redirect('home')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})
