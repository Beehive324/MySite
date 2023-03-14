#django imports

from django.db import models
from datetime import datetime
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

# def upload_location(instance, filename):
#     file_path = 'blog/{artist_id}/{title}-{filename}'.format(
#         artist_id=str(instance.artist.id), title=str(instance.title), filename=filename
#     )
#     return file_path

# A class to store details of my blog articles

#Music class with the following attributes
class Music(models.Model):
    image = models.ImageField(null=False, blank=False)
    title = models.CharField(max_length=100) # Title of the article
    genre = models.CharField(max_length=2000) # Main text of the article
    artist = models.CharField(max_length=100) # Name of the author
    date_created = models.DateTimeField(default=datetime.now, blank=True)


    # cover_image = models.ImageField(upload_Location=upload_location, null=False, blank=False)
    # date = models.DateTimeField(auto_now_add=True, verbose_name="date published")



    def __str__(self):
        return self.title # returns title statement

 


