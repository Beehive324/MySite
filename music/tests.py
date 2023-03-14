from django.test import TestCase
from django.test import SimpleTestCase
from django.db.backends.sqlite3.base import IntegrityError
from django.db import transaction
from django.urls import reverse, resolve
from collection.views import 




class MusicTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        n1= Music(title= "Low down")
        n1.save()


class TestUrls(SimpleTestCase):

    def test_list_url(self):
        assert 1 == 2