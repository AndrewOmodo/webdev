from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewTasKForm(forms.Form):
    task = forms.ChoiceField(label="New task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasks"],
    }),

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpReponseRedirect(reverse("tasks:index"))
        else: 
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTasKForm()
    })