from django.db import models
from django.contrib.auth.models import User

# Create your models here.

COUNTRY_CHOICES = (('usa', 'США'), ('japan', 'Япония'), ('kr', 'Юж.Корея'),)


class OnlyNameModel(models.Model):
    name = models.CharField(max_length=255)
    
    
    class Meta:
        abstract = True

    def __str__(self):
            return str(self.name)

class Genre(OnlyNameModel):
    pass

class Collection(OnlyNameModel):
    pass


class MovieParticipant(models.Model):
    image = models.ImageField(upload_to="movie_participant/")
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES ) 

    class Meta:
        abstract = True
    
    
    
    
    def __str__(self):
        return f"{self.first_name} {self.middle_name if self.middle_name else ""} {self.last_name} ({self.country})"

class MovieDirector(MovieParticipant):
    pass

class MovieActor(MovieParticipant):
    pass


class Movie(models.Model):
    RATING_CHOICES = (
        ("G", "G"),
        ("PG", "PG"),
        ("PG-13", "PG-13"),
        ("R", "R"),
        ("NC-17", "NC-17"),
    )
    cover = models.ImageField(upload_to="movie_covers/")
    title = models.CharField(max_length=255)
    rating = models.CharField(max_length=6, choices=RATING_CHOICES)
    date_of_release = models.DateField()
    date_of_running = models.DateField()
    date_of_running_end = models.DateField()
    time = models.PositiveIntegerField()
    description = models.TextField(max_length=1000)
    genre = models.ManyToManyField(Genre)
    collection = models.ManyToManyField(Collection)
    trailer_url = models.URLField()


    def __str__(self):
        return f"{self.title} ({self.date_of_release})"



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=1000)
    reting = models.FloatField()

    def __str__(self):
        return f"{self.user.username} поставил оценку {self.rating} на фильм {self.movie.title} ({self.movie.date_of_release})"




