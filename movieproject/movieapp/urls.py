from django.urls import path
from . import views

app_name = 'movieapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>', views.details, name='details'),
    path('add/', views.addmovie, name='addmovie'),
    path('update/<int:movie_id>/', views.updatemovie, name='updatemovie'),
    path('delete/<int:movie_id>/', views.deletemovie, name='deletemovie'),
]
