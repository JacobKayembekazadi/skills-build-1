from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')
        team1.members.add(user1)
        team1.members.add(user2)
        team2.members.add(user3)

        # Activities
        activity1 = Activity.objects.create(user=user1, type='run', duration=30, date='2025-05-31T10:00:00Z')
        activity2 = Activity.objects.create(user=user2, type='walk', duration=45, date='2025-05-31T11:00:00Z')
        activity3 = Activity.objects.create(user=user3, type='strength', duration=60, date='2025-05-31T12:00:00Z')

        # Leaderboard
        Leaderboard.objects.create(team=team1, points=150)
        Leaderboard.objects.create(team=team2, points=100)

        # Workouts
        Workout.objects.create(user=user1, description='Pushups', date='2025-05-31T10:30:00Z')
        Workout.objects.create(user=user2, description='Situps', date='2025-05-31T11:30:00Z')
        Workout.objects.create(user=user3, description='Squats', date='2025-05-31T12:30:00Z')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
