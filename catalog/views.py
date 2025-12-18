from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Movie, Collection, Genre, Premiere, FavoriteMovie
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout




def main_page(request):
    collections = Collection.objects.all()
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    premieres = Premiere.objects.all()


    if request.method == "POST":
        movie_id = request.POST.get('movie_id')
        current_movie = Movie.objects.get(id=movie_id)
        is_favorite = FavoriteMovie.objects.filter(user=request.user, movie=current_movie).exists()


        if is_favorite == False:
            FavoriteMovie.objects.create(movie=current_movie, user=request.user)

    context = {
        'movies': movies,
        'collections': collections,
        'genres': genres,
        'premieres': premieres,
        'user' : User
    }

    return render(request, 'index.html', context)


def profile_page(request):
    user = request.user
    favorite_movies = FavoriteMovie.objects.filter(user=user)
    context = {
        'user' : user,
        'favorite_movies' : favorite_movies
    }
 


    return render(request, 'profile.html', context)

def register_view(request):
    context = {
        'error': []
    }

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if username and password and confirm and password == confirm:
            user_from_db = authenticate(request, username=username, password=password)

            if user_from_db is None:
                
                User.objects.create(
                    username=username,
                    password=make_password(password)
                )
                return redirect('login_view')
            else:
                context['error'].append('Ошибка! Пользователь с таким логином уже существует')
        else:
            context['error'].append('Ошибка! Введите данные правильно')

    return render(request, 'register.html', context)

def login_view(request):
    context = {
        'error': []
    }
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user_from_db = authenticate(request,username=username,password=password)
            if user_from_db is not None:
                login(request,user_from_db)
                return redirect('main_page')
            else:
                context['error'].append("Ошибка ! Пользователь с таким логином не сушествует")
        else:
            context['error'].append("Ошибка ! Введите данные правильно")
            
    return render(request, 'login.html', context)
def logout_view(request):
    logout(request)
    return redirect('main_page')