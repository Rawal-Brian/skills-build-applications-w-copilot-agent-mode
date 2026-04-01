#!/usr/bin/env python
import os
import sys
import django

# Add the backend to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'octofit-tracker/backend'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import Activity, Workout, LeaderboardEntry, User, Team

print(f'Users: {User.objects.count()}')
print(f'Teams: {Team.objects.count()}')
print(f'Activities: {Activity.objects.count()}')
print(f'Workouts: {Workout.objects.count()}')
print(f'Leaderboard: {LeaderboardEntry.objects.count()}')

if Activity.objects.exists():
    print('\nFirst activity:')
    act = Activity.objects.first()
    print(f'  ID: {act.id}')
    print(f'  Type: {act.type}')
    print(f'  User ID: {act.user_id}')
    print(f'  User: {act.user}')
    print(f'  Team ID: {act.team_id}')
    print(f'  Team: {act.team}')
