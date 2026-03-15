from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='dc')
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='dc')

        # Create teams with member emails
        marvel = Team.objects.create(name='marvel', members='ironman@marvel.com,captain@marvel.com')
        dc = Team.objects.create(name='dc', members='batman@dc.com,superman@dc.com')

        # Create activities using user_email
        Activity.objects.create(user_email='ironman@marvel.com', type='run', duration=30, date='2026-03-14')
        Activity.objects.create(user_email='batman@dc.com', type='cycle', duration=45, date='2026-03-14')
        Activity.objects.create(user_email='captain@marvel.com', type='swim', duration=20, date='2026-03-14')
        Activity.objects.create(user_email='superman@dc.com', type='fly', duration=60, date='2026-03-14')

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
