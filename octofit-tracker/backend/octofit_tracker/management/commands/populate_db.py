from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Example models for demonstration (should be replaced with actual models)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (superheroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', first_name='Peter', last_name='Parker'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', first_name='Clark', last_name='Kent'),
        ]

        # Create activities
        Activity.objects.create(user='ironman', activity_type='Running', duration=30)
        Activity.objects.create(user='spiderman', activity_type='Cycling', duration=45)
        Activity.objects.create(user='batman', activity_type='Swimming', duration=60)
        Activity.objects.create(user='superman', activity_type='Yoga', duration=20)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=80)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility.')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
