from django.shortcuts import render, redirect
from .models import ToDoItem, Users
from .forms import CreateNewList, EnterUser


# Create your views here.

def home_page(request):
    if request.method == "POST":
        form = EnterUser(request.POST)

        if form.is_valid():
            user = form.cleaned_data["name"]
            Users.objects.all().delete()
            Users(name=user).save()

            return redirect('view')

    else:
        form = EnterUser()

    return(render(request, "home.html", {"form": form}))

def add_items(request):

    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            form_n = form.cleaned_data["user_name"]
            form_t = form.cleaned_data["title"]
            form_completed = form.cleaned_data["completed"]

            t = ToDoItem(user_name=form_n, title=form_t, completed=form_completed)
            t.save()

            form = CreateNewList()

    else:
        form = CreateNewList()

    return(render(request, "add.html", {"form": form}))

def view_items(request):
    return(render(request, "view.html", {"name": Users.objects.first(), "todos": ToDoItem.objects.all()}))