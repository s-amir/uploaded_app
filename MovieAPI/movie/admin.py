from django.contrib import admin

# Register your models here.
from movie.models import Movie

from django.contrib.auth.models import Group  # new


# ...
# admin.site.unregister(Group)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'image_tag', 'movie_genre', 'description', 'image_url', 'release_date', 'idbm_score')
    editable_list = ['idbm_score']           #!!!!!!!!!!!!!
    search_fields = ('movie_title', 'description')
    list_filter = ['movie_genre', 'idbm_score']


    admin.site.site_header = "Tesco Box Project"
    admin.site.site_title = "test mode"

# admin.site.register(Movie)
