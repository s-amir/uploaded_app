from django.contrib import admin

# Register your models here.
from movie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_title','description',' movie_genre','image_url','release_date','idbm_score')

# admin.site.register(Movie)