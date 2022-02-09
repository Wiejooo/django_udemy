from django.urls import path
from .views import all_films, empty_page

urlpatterns = [
    path('all/', all_films),
    path('', empty_page),
]