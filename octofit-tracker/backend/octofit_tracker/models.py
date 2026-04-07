from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields can be added here
    pass

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('User', related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.FloatField()  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in km
    calories = models.FloatField(null=True, blank=True)
    date = models.DateTimeField()

class Workout(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class LeaderboardEntry(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='leaderboard_entries')
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='leaderboard_entries')
    score = models.FloatField()
    rank = models.IntegerField()
    period = models.CharField(max_length=20)  # e.g., 'weekly', 'monthly'
    updated_at = models.DateTimeField(auto_now=True)
