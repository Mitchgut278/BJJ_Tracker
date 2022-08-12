from tkinter import CASCADE
from django.contrib.auth.models import User
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    date = models.DateTimeField(auto_now=True)
    steps = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class MOTD(models.Model):
    
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)

    
    class Meta:
        # Can only have 1 MOTD per user per day (UNIQUE Constraint)
        unique_together=['date','user']
