from django.contrib import admin
from projects.models import *
from userAuth.models import *
# Register your models here.

admin.site.register(Projects)
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(UserPhone)

