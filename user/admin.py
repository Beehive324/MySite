from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


class UserAdminstration(UserAdmin):
    list_display = ('email', 'username')
    search_fields = ('email', 'username')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdminstration) 

