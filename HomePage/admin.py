from django.contrib import admin
from projects.models import *
from user.models import UserPhone
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Projects)
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(Tag)
# admin.site.register(UserPhone)

