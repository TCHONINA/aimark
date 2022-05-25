from datetime import datetime

from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login

# Create your views here.
from aimark.forms import MarqueForm
from aimark.models import Mark, Point


def add(request):
    if request.method == 'POST':
        form = MarqueForm(request.POST, request.FILES)
        if form.is_valid():
            mark = Mark(name=form.cleaned_data['title'],
                        image=form.cleaned_data['image']
                        , created_at=datetime.today())
            mark.save()

        return redirect('/mark/edit/' + str(mark.id))
    else:
        marks = Mark.objects.all()
        form = MarqueForm()

        return render(request, 'addmark.html', {'marks': marks, 'form': form})


def edit(request, id):
    mark = Mark.objects.get(id=id)
    if request.method == 'POST':
        form = MarqueForm(request.POST, request.FILES)
        if form.is_valid():

            # mark.user = request.user.id
            mark.name = form.cleaned_data['title']
            if form.cleaned_data['image']:
                mark.image = form.cleaned_data['image']

            mark.save()

        return redirect('/mark/edit/' + str(id))

    else:
        form = MarqueForm(initial={
            'id': mark.id,
            'title': mark.name,
            'image': mark.image,
            'created_at': mark.created_at,
        })
        points = Point.objects.filter(mark=id)

        return render(request, 'editmark.html', {'form': form, 'points': points})


def addpoint(request, id):
    if request.method == 'POST':
        # HttpResponse(request.POST['x'])
        point = Point(mark=Mark.objects.get(id=id), num=request.POST['count'], x=request.POST['x']
                      , y=request.POST['y'])
        point.save()
        return HttpResponse('good')
    else:
        return redirect('/admins/marks/')


def temp_exemple(request):
    return render(request, "child.html")


def loginPage(request):
    if request.method == 'POST':
        us = request.POST.get('user')
        ps = request.POST.get('pass')
        user = authenticate(request, username=us, password=ps)
        if user is not None:
           login(request, user)
           return redirect('home')
    else:
        messages.error(request, "Login or pass isnt correcte")
    return render(request, "login.html")


def deletepoint(request, id):
    Point.objects.filter(mark=id).delete()
    return redirect('/mark/edit/' + str(id))


def delete(request, id):
    Mark.objects.filter(id=id).delete()
    return redirect('/mark/add')


def recherche(request):
    m = request.GET.get("search", "")
    marks = Mark.objects.filter(name__contains=m)
    context = {'marks': marks}
    return render(request, 'addmark.html', context)


######################"# Home page ###############################
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return redirect('/login')


######################"# Auth ###############################


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/mark/add')
    else:
        return render(request, "login.html")


def loginclick(request):
    if (request.method == 'POST'):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/mark/add')
        else:
            messages.error(request, 'username our mot de passe est inccorect')
            # messages.error(request,request.POST['username']+" "+request.POST['password'])
            return redirect('/login')
    else:
        messages.error(request, 'login again')

        return redirect('/login')


def logoutclick(request):
    if (request.user.is_authenticated and request.method == 'POST'):
        logout(request)
        return redirect('/login')
    else:
        return redirect('/')
