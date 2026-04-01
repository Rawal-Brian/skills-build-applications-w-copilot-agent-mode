#!/usr/bin/env python
import os
import sys
import django

# Add the backend to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'octofit-tracker/backend'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import Activity, Workout, LeaderboardEntry, User, Team
from django.utils import timezone

try:
    # Clear existing data
    Activity.objects.all().delete()
    Workout.objects.all().delete()
    LeaderboardEntry.objects.all().delete()
    
    print("Cleared old data")
    
    # Get teams
    teams = list(Team.objects.all()[:2])
    marvel = teams[0]
    dc = teams[1] if len(teams) > 1 else teams[0]
    
    # Get users
    users = list(User.objects.all()[:4])
    if len(users) >= 4:
        ironman, spiderman, batman, superman = users[0:4]
    else:
        print(f"Only {len(users)} users available, need 4")
        sys.exit(1)
    
    print(f"Using teams: {marvel.name}, {dc.name}")
    print(f"Using users: {ironman.username}, {spiderman.username}, {batman.username}, {superman.username}")
    
    # Create activities
    act1 = Activity(user_id=ironman.id, type='Running', duration=30, calories=300, date=timezone.now())
    act1.save()
    print(f"Created activity 1: {act1.id}")
    
    act2 = Activity(user_id=spiderman.id, type='Cycling', duration=45, calories=450, date=timezone.now())
    act2.save()
    print(f"Created activity 2: {act2.id}")
    
    act3 = Activity(user_id=batman.id, type='Swimming', duration=60, calories=600, date=timezone.now())
    act3.save()
    print(f"Created activity 3: {act3.id}")
    
    act4 = Activity(user_id=superman.id, type='Yoga', duration=20, calories=200, date=timezone.now())
    act4.save()
    print(f"Created activity 4: {act4.id}")
    
    # Create workouts
    w1 = Workout(user_id=ironman.id, name='Hero HIIT', description='High intensity interval training for heroes.')
    w1.save()
    print(f"Created workout 1: {w1.id}")
    
    w2 = Workout(user_id=batman.id, name='Power Yoga', description='Yoga for strength and flexibility.')
    w2.save()
    print(f"Created workout 2: {w2.id}")
    
    # Create leaderboard entries
    lb1 = LeaderboardEntry(user_id=ironman.id, score=75, rank=1, period='weekly')
    lb1.save()
    print(f"Created leaderboard 1: {lb1.id}")
    
    lb2 = LeaderboardEntry(user_id=spiderman.id, score=60, rank=2, period='weekly')
    lb2.save()
    print(f"Created leaderboard 2: {lb2.id}")
    
    lb3 = LeaderboardEntry(user_id=batman.id, score=85, rank=1, period='weekly')
    lb3.save()
    print(f"Created leaderboard 3: {lb3.id}")
    
    lb4 = LeaderboardEntry(user_id=superman.id, score=70, rank=2, period='weekly')
    lb4.save()
    print(f"Created leaderboard 4: {lb4.id}")
    
    print("\n✅ All data created successfully!")
    print(f"Activities: {Activity.objects.count()}")
    print(f"Workouts: {Workout.objects.count()}")
    print(f"Leaderboard: {LeaderboardEntry.objects.count()}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
