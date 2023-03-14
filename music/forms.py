from django import forms

from collection.models import Music

class MusicForm(forms.ModelForm): # class defining the music form
    class Meta:
        model = Music
        fields = ['image', 'artist', 'title', 'genre']
     