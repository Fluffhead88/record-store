from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import User, Band, Album

admin.site.register(User, UserAdmin)
admin.site.register(Band)
admin.site.register(Album)
