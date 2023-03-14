from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from django.contrib import admin
from django.urls import path, include

from collection.views import showMusic

from django.conf import settings
from django.conf.urls.static import static

from collection.views import home_page_view
from collection.views import link_view
from collection.views import showMusic
from collection.views import musicdetail
from user.views import contact_view
from collection.views import searchBar
from music.views import addMusic

from user.views import login_view

from user.views import (
    reg_view,
    logout_view,
    login_view,
    user_view,
)



class MusicTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        n1= Music(title= "Low down", genre = "Hip Hop", artist = "Lil Baby")
        n1.save()
        n2 =Music(title= "Slayin", genre = "Hip Hop", artist = "Black Kray")
        n2.save()

def test_homepage(self): #home page test
    response = self.client.get('/home')
    self.assertEqual(response.status_code, 200)

    self.assertContains(response, 'This is my Home Page')
    self.assertContains(response, 'This is my footer')


class TestUrls(SimpleTestCase):  # tests for url views

    def test_list_url_is_resolved(self):
        url = reverse('list')
        print(resolve(url))


def test_save_music(self): #
    db_count = Music.objects.all().count()
    music = Music('title=New Song', genre="New genre", artist="New artist")
    music.save()
    self.assertEqual(db_count+1, Music.objects.all().count())

def test_duplicate_title(self):
    db_count = Music.objects.all().count()
    music = Music(title='1st Song', genre="Random", artist="New artist")
    try:
        with transaction.atomic():
            music.save()
        except IntegrityError:
            pass
        self.assertNotEqual(db_count+1, Music.objects.all().count())


def test_post_create(self):
    db_count = Music.objects.all().count()
    data = {
        "title": "new song",
        "genre": "new genre",
    }

    response = self.client.post(reverse('notes_new'), data=data)
    self.assertEqual(Music.objects.count(, db_count+1)