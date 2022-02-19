from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Create users to test'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        # User.objects.all().delete()
        count = options['count']
        for i in range(count):
            user = User.objects.create(
                username=f'uname{i}',
                first_name=f'fname{i}',
                last_name=f'lname{i}',
                email=f'user{i}@gb.local')
            print(f'author {user.first_name} created')
        print('done')
