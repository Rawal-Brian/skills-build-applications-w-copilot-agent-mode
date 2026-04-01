from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Workout, LeaderboardEntry
from django.utils import timezone

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        try:
            # Clear only data tables
            LeaderboardEntry.objects.all().delete()
            Activity.objects.all().delete()
            Workout.objects.all().delete()
            
            # Get teams (or create if none exist)
            teams = Team.objects.all()[:2]
            if not teams or len(teams) < 2:
                Team.objects.all().delete()
                marvel = Team.objects.create(name='Marvel')
                dc = Team.objects.create(name='DC')
                teams = [marvel, dc]
            else:
                marvel, dc = teams[0], teams[1]

            # Get users 
            users = User.objects.exclude(is_superuser=True, is_staff=True)[:4]
            if users:
                ironman, spiderman, batman, superman = users[0], users[1], users[2], users[3]
            else:
                # Create them if none exist
                ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark')
                spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', first_name='Peter', last_name='Parker')
                batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne')
                superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', first_name='Clark', last_name='Kent')

            # Create activities
            Activity.objects.create(user=ironman, team_id=str(marvel.pk), type='Running', duration=30, calories=300, date=timezone.now())
            Activity.objects.create(user=spiderman, team_id=str(marvel.pk), type='Cycling', duration=45, calories=450, date=timezone.now())
            Activity.objects.create(user=batman, team_id=str(dc.pk), type='Swimming', duration=60, calories=600, date=timezone.now())
            Activity.objects.create(user=superman, team_id=str(dc.pk), type='Yoga', duration=20, calories=200, date=timezone.now())

            # Create workouts
            Workout.objects.create(user=ironman, name='Hero HIIT', description='High intensity interval training for heroes.')
            Workout.objects.create(user=batman, name='Power Yoga', description='Yoga for strength and flexibility.')

            # Create leaderboard entries
            LeaderboardEntry.objects.create(user=ironman, team_id=str(marvel.pk), score=75, rank=1, period='weekly')
            LeaderboardEntry.objects.create(user=spiderman, team_id=str(marvel.pk), score=60, rank=2, period='weekly')
            LeaderboardEntry.objects.create(user=batman, team_id=str(dc.pk), score=85, rank=1, period='weekly')
            LeaderboardEntry.objects.create(user=superman, team_id=str(dc.pk), score=70, rank=2, period='weekly')

            self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error populating database: {str(e)}'))
            import traceback
            traceback.print_exc()
