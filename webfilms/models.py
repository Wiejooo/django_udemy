from django.db import models

empty_description = 'Chwilowy brak opisu.'


class Films(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default=empty_description, blank=True)
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    picture = models.ImageField(upload_to='picture', null=True, blank=True)

    def __str__(self):
        return f'{self.title} ({self.year})'

