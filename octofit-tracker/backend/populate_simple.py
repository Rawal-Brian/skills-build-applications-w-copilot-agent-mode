#!/usr/bin/env python
"""
Simple script to populate MongoDB with sample data using direct MongoDB connection
"""
from pymongo import MongoClient
from datetime import datetime, timedelta
import uuid

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Clear existing collections
db['octofit_tracker_user'].delete_many({})
db['octofit_tracker_team'].delete_many({})
db['octofit_tracker_activity'].delete_many({})
db['octofit_tracker_workout'].delete_many({})
db['octofit_tracker_leaderboardentry'].delete_many({})

print("Cleared existing data...")

# Create teams
marvel_team = {
    'id': 1,
    'name': 'Marvel',
    'created_at': datetime.now()
}
dc_team = {
    'id': 2,
    'name': 'DC',
    'created_at': datetime.now()
}
db['octofit_tracker_team'].insert_many([marvel_team, dc_team])
print("Teams created...")

# Create users (without password hashing for simplicity)
users = [
    {
        'id': 1,
        'username': 'ironman',
        'email': 'ironman@marvel.com',
        'first_name': 'Tony',
        'last_name': 'Stark',
        'is_active': True,
        'is_staff': False,
        'is_superuser': False,
        'date_joined': datetime.now(),
    },
    {
        'id': 2,
        'username': 'spiderman',
        'email': 'spiderman@marvel.com',
        'first_name': 'Peter',
        'last_name': 'Parker',
        'is_active': True,
        'is_staff': False,
        'is_superuser': False,
        'date_joined': datetime.now(),
    },
    {
        'id': 3,
        'username': 'batman',
        'email': 'batman@dc.com',
        'first_name': 'Bruce',
        'last_name': 'Wayne',
        'is_active': True,
        'is_staff': False,
        'is_superuser': False,
        'date_joined': datetime.now(),
    },
    {
        'id': 4,
        'username': 'superman',
        'email': 'superman@dc.com',
        'first_name': 'Clark',
        'last_name': 'Kent',
        'is_active': True,
        'is_staff': False,
        'is_superuser': False,
        'date_joined': datetime.now(),
    }
]
db['octofit_tracker_user'].insert_many(users)
print("Users created...")

# Create activities
activities = [
    {
        'id': 1,
        'user': 1,  # ironman
        'team': 1,  # marvel
        'type': 'Running',
        'duration': 30.0,
        'distance': 5.0,
        'calories': 300.0,
        'date': datetime.now()
    },
    {
        'id': 2,
        'user': 2,  # spiderman
        'team': 1,  # marvel
        'type': 'Cycling',
        'duration': 45.0,
        'distance': 15.0,
        'calories': 450.0,
        'date': datetime.now()
    },
    {
        'id': 3,
        'user': 3,  # batman
        'team': 2,  # dc
        'type': 'Swimming',
        'duration': 60.0,
        'distance': 2.0,
        'calories': 600.0,
        'date': datetime.now()
    },
    {
        'id': 4,
        'user': 4,  # superman
        'team': 2,  # dc
        'type': 'Yoga',
        'duration': 20.0,
        'distance': None,
        'calories': 200.0,
        'date': datetime.now()
    }
]
db['octofit_tracker_activity'].insert_many(activities)
print("Activities created...")

# Create workouts
workouts = [
    {
        'id': 1,
        'user': 1,  # ironman
        'name': 'Hero HIIT',
        'description': 'High intensity interval training for heroes.',
        'suggested': True,
        'created_at': datetime.now()
    },
    {
        'id': 2,
        'user': 3,  # batman
        'name': 'Power Yoga',
        'description': 'Yoga for strength and flexibility.',
        'suggested': False,
        'created_at': datetime.now()
    }
]
db['octofit_tracker_workout'].insert_many(workouts)
print("Workouts created...")

# Create leaderboard entries
leaderboard = [
    {
        'id': 1,
        'user': 1,  # ironman
        'team': 1,  # marvel
        'score': 75.0,
        'rank': 1,
        'period': 'weekly',
        'updated_at': datetime.now()
    },
    {
        'id': 2,
        'user': 2,  # spiderman
        'team': 1,  # marvel
        'score': 60.0,
        'rank': 2,
        'period': 'weekly',
        'updated_at': datetime.now()
    },
    {
        'id': 3,
        'user': 3,  # batman
        'team': 2,  # dc
        'score': 85.0,
        'rank': 1,
        'period': 'weekly',
        'updated_at': datetime.now()
    },
    {
        'id': 4,
        'user': 4,  # superman
        'team': 2,  # dc
        'score': 70.0,
        'rank': 2,
        'period': 'weekly',
        'updated_at': datetime.now()
    }
]
db['octofit_tracker_leaderboardentry'].insert_many(leaderboard)
print("Leaderboard entries created...")

client.close()
print("✓ Database populated successfully with sample data!")
