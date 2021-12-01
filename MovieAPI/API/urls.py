from django.urls import path

from API import views

urlpatterns=[
    path('movieById/', views.getMovieById),
    path('movies/', views.getMovies),
]