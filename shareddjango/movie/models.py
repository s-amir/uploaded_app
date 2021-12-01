from django.db import models

# Create your models here.
class Movie(models.Model):
    STATUS_CHOICE = (
        ('comedy', 'Comedy'),
        ('action', 'Action'),
        ('animation', 'Animation'),
        ('horror', 'Horror'),
        ('science_fiction', 'Science'),

    )
    movie_title=models.CharField(max_length=30)
    description=models.TextField(max_length=450)
    movie_genre=models.CharField(max_length=30,choices=STATUS_CHOICE)
    image_url=models.ImageField(upload_to='uploads/')
    release_date=models.DateField(auto_now_add=True)
    idbm_score=models.FloatField(max_length=10.0,default=8)

    def __str__(self):
     return self.movie_title