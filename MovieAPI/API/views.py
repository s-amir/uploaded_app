from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_protect
from rest_framework import response, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from API.serializer.movieSerializer import MovieSerializer
from movie.models import Movie


# get a movies by id  --functionbase
@api_view(['POST', ])
def getMovieById(request):
    id = request.POST['pk']  # id of input is pk!!!
    try:
        movie = Movie.objects.get(pk=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# get list of movies --functionbase

@csrf_protect
@api_view(['GET', ])
def getMovies(request):
    try:
        movies = Movie.objects.all()
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# ClassBase
class APIList(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True,)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
