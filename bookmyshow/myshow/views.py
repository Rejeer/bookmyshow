# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.db import IntegrityError

from . models import Profile

from .models import Show
def movieList(request):
    show = Show.objects.all()
    context = {'Show': show}
    return render(request, 'index.html', context)

def createMovie(request):
    if request.method == "POST":
        movies = request.POST.get('movies')
        actor = request.POST.get('actor')
        director = request.POST.get('director')
        gene = request.POST.get('gene')
        image = request.FILES.get('image')
        show = Show.objects.create(movies=movies, actor=actor, director=director, genres=gene, image=image,fk_user=request.user)
        show.save()
        return redirect('index')
    context = {'gen': Show.gen_choice}
    return render(request, 'create_movie.html', context)

def movieDetails(request, show_id):
    movie_obj = Show.objects.get(id=show_id)
    context = {'show': movie_obj}
    return render(request, 'movie_details.html', context)

def movieEdit(request, show_id):
    show = Show.objects.get(id=show_id)
    if request.method == 'POST':
        movies = request.POST.get('movies')
        director = request.POST.get('director')
        actor = request.POST.get('actor')
        gene = request.POST.get('gene')
        image = request.FILES.get('image')
        if movies:
            show.movies = movies
        if director:
            show.director = director
        if actor:
            show.actor = actor
        if gene:
            show.genres = gene
        if image:
            show.image = image
        show.save()
        return redirect('detail', show.id)
    context = {'show': show, 'gen': Show.gen_choice,}
    return render(request, 'edit.html', context)

def movieDelete(request, show_id):
    show = Show.objects.get(id=show_id)
    if request.method == 'POST':
        show.delete()
        return redirect('index')
    messages.error(request,'Show deletion failed....')
    context = {'show': show}
    return render(request, 'movie_delete.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create_user(username=username,email=email,password=password2)
            user.save()
            messages.success(request,'Registration successfully')
            return redirect('index')
        
        messages.error(request,"password doesn't match. Please try agian..")
    return render(request,'signup.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print('username',username)
        password = request.POST.get('password')
        print('password',password)
        user= authenticate(username=username,password=password)
        print('user',user)
        if user:
            login(request,user)
            messages.success(request,'successfully Logged')
            return redirect('index')
        messages.error(request,'usern does not exist ... "Please Register.."' )
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    messages.success(request,'Successfully..')
    return redirect('login')

 
def userCreate(request):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        location = request.POST.get('location')
        image = request.POST.get('image')
        profile = Profile.objects.create(bio=bio, location=location, image=image)
        profile.save()
        return redirect('index')
    return render(request, 'create_profile.html')


def userDetails(request,id):
    # user_obj = Profile.objects.get(id=user_id)
    user_profile = get_object_or_404(Profile, id=id)
    return render(request, 'user_details.html', {'profile': user_profile})
    # context = {'user':user_obj}
    # return render(request,'user_details.html',context)

        



