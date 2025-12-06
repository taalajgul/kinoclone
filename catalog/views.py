from django.shortcuts import render
from .models import Movie , Collection


def main_page(request):
    collections = Collection.objects.all()
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
        'collections' : collections
    }
    
    
    return render(request, 'index.html',context)