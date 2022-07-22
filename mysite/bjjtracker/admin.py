from django.contrib import admin
from .models import Position, Technique, Tag

# Register your models here.
admin.site.register(Position)
admin.site.register(Technique)
admin.site.register(Tag)