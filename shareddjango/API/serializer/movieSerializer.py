from rest_framework import serializers

from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Movie
        fields = ['id','movie_title','description','movie_genre','release_date','idbm_score','image_url']

    def get_image_url(self, obj):
        return obj.image_url.url[1:]
