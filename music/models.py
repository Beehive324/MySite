# from django.db import models


# from django.db.models.signals import pre_save
# from django.utils.text import slugify
# from django.conf import settings
# from django.db.models.signals import post_delete, pre_Save
# from django.dispatch import receiver


# def upload_Location(instance, filename):
#     file_pathway ='blog'/{artist_id}/{title}-{filename}'.format(artist_id=str(instance.artist.id), title=str(instance.title), filename=filename)
#     return file_pathway



# class MusicPost(models.Model):
#     title = models.CharFieldd(max_length=50, null=False, blank=False)
#     main = models.TextField(max_Length=5000, null=False, blank=False)
#     image = models.ImageField(upload_Location=upload_Location, null=False, blank=False)
#     date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
#     date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
#     url = models.SlugField(blank=True, unique=True)

#     def __str__(self):
#         return self.title
    
# @receiver(post_delete, sender=BlogPost)
# def submission_delete(sender, instance):
#     instance.iamge.delete(False)






