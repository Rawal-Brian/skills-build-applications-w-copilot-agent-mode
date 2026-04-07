#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import Team, User
from django.utils import timezone

# Create teams only
Team.objects.create(name='Marvel')
Team.objects.create(name='DC')
Team.objects.create(name='Avengers')

# Create users only
User.objects.create_user(
    username='ironman',
    email='ironman@marvel.com',
    password='password123',
    first_name='Tony',
    last_name='Stark'
)

User.objects.create_user(
    username='spiderman',
    email='spiderman@marvel.com',
    password='password123',
    first_name='Peter',
    last_name='Parker'
)

User.objects.create_user(
    username='batman',
    email='batman@dc.com',
    password='password123',
    first_name='Bruce',
    last_name='Wayne'
)

User.objects.create_user(
    username='superman',
    email='superman@dc.com',
    password='password123',
    first_name='Clark',
    last_name='Kent'
)

print("Sample data loaded successfully!")

