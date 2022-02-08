from django.contrib import admin
from .models import Films

# admin.site.register(Films)


@admin.register(Films)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'year']
    list_filter = ('year', )
    search_fields = ('title', )