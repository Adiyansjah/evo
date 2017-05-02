from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserDetail


class UserDetailInline(admin.StackedInline):
    model = UserDetail


class UserDetailAdmin(UserAdmin):
    inlines = [UserDetailInline]


admin.site.unregister(User)
admin.site.register(User, UserDetailAdmin)
