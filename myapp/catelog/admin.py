from django.contrib import admin
from .models import album,song,awards

# Register your models here.
admin.site.register(album)
admin.site.register(song)
admin.site.register(awards)

