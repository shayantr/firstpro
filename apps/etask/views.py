from django.shortcuts import render, reverse
from django import forms
from django.http import *


class NewTaskForm(forms.Form):
    task = forms.CharField(max_length=64)
# Create your views here.


def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []
    return render(request, 'etask/index.html', {
        'tasks': request.session['tasks'],
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
            return HttpResponseRedirect(reverse('etask:index'))
    else:
        form = NewTaskForm()
    return render(request, "etask/add.html", {
        "form": form,
    })

