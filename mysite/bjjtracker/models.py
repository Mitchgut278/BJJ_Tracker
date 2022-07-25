from tkinter import CASCADE
from turtle import position
from django.db import models
import uuid

# Create your models here.
class Position(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    concepts = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Technique(models.Model):
    TOP_BOTTOM = (
        ('top', 'top'),
        ('bottom', 'bottom'),
    )
    name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    topBottom = models.CharField(max_length=10, choices=TOP_BOTTOM, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    date = models.DateTimeField(auto_now=True)
    steps = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name