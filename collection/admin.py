from django.contrib import admin
from collection.models import Music

# Register your models here.

class MusicAdmin(admin.ModelAdmin): # This is the music admin class displaying all the fields for the class
    list_display = ('title', 'genre', 'artist')
    list_display_links =('title','genre')
    list_filter = ('genre','artist')
    search_fields = ('name', 'genre')
    ordering = ('genre','artist')




admin.site.register(Music, MusicAdmin) # Registers the admin site to Music and MusicAdmin
