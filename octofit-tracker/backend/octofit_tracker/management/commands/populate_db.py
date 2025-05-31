from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the database with initial test data for OctoFit Tracker'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating users...')
        # Create test users
        users = [
            User.objects.create(email='john.smith@mergington.edu', name='John Smith', password='secure123'),
            User.objects.create(email='emma.wilson@mergington.edu', name='Emma Wilson', password='secure123'),
            User.objects.create(email='michael.brown@mergington.edu', name='Michael Brown', password='secure123'),
            User.objects.create(email='sarah.davis@mergington.edu', name='Sarah Davis', password='secure123'),
            User.objects.create(email='james.miller@mergington.edu', name='James Miller', password='secure123'),
        ]

        self.stdout.write('Creating teams...')
        # Create teams
        teams = [
            Team.objects.create(name='Lightning Bolts'),
            Team.objects.create(name='Power Rangers'),
            Team.objects.create(name='Fitness Warriors')
        ]

        # Assign users to teams
        teams[0].members.add(users[0], users[1])  # Lightning Bolts
        teams[1].members.add(users[2], users[3])  # Power Rangers
        teams[2].members.add(users[4])            # Fitness Warriors

        self.stdout.write('Creating activities...')
        # Create activities with recent dates
        activity_types = ['Running', 'Walking', 'Swimming', 'Cycling', 'Weight Training']
        now = timezone.now()
        
        for user in users:
            for i in range(3):  # 3 activities per user
                activity_date = now - timedelta(days=i)
                Activity.objects.create(
                    user=user,
                    type=activity_types[i % len(activity_types)],
                    duration=30 + (i * 15),  # Varying durations
                    date=activity_date
                )

        self.stdout.write('Creating leaderboard entries...')
        # Create leaderboard entries
        points = [1500, 1200, 900]  # Different points for different teams
        for team, point in zip(teams, points):
            Leaderboard.objects.create(team=team, points=point)

        self.stdout.write('Creating workouts...')
        # Create workout entries
        workout_descriptions = [
            'Morning cardio: 30 min run, 20 pushups, 30 situps',
            'Weight training: bench press, squats, deadlifts',
            'HIIT workout: burpees, mountain climbers, jumping jacks',
            'Yoga and stretching routine',
            'Swimming laps and water aerobics'
        ]

        for user in users:
            for i in range(2):  # 2 workouts per user
                workout_date = now - timedelta(days=i)
                Workout.objects.create(
                    user=user,
                    description=workout_descriptions[i % len(workout_descriptions)],
                    date=workout_date
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated database with test data for OctoFit Tracker'))
