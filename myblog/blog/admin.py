from django.contrib import admin

from .models import Tag,Blog

admin.site.register(Blog)
admin.site.register(Tag)
