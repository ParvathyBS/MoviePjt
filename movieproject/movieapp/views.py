from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'ml': movie
    }
    return render(request, 'index.html', context)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def addmovie(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        image = request.FILES['image']
        year = request.POST.get('year', )
        desc = request.POST.get('desc', )
        movie = Movie(name=name, image=image, year=year, desc=desc)
        movie.save()
    return render(request, 'add_movie.html')


def updatemovie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'updatemovie.html', {'form': form, 'movie': movie})


def deletemovie(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request, 'deletemovie.html')
