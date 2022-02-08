from django.db import models


class Films(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default='')
    premiere = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} ({self.year})'
