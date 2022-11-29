from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(blog)
admin.site.register(Userlogin)
admin.site.register(BookMark)
admin.site.register(Comment)