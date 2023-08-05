from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(Magazine)
admin.site.register(Article)