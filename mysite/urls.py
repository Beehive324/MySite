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

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('music.urls')),
    path('', home_page_view, name='home'),
    path('register/', reg_view, name="register",),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('user/', user_view, name="user"),
    path('link/', link_view, name="links"),
    path('login/', login_view, name="login"),
    path('contact/', contact_view, name="contact"),
    path('music/', showMusic, name='Music'),
    path('musicdetail/', musicdetail, name='musicDetail'),
    path('search/', searchBar, name='search'),
    path('addMusic/', addMusic, name='addMusic'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

