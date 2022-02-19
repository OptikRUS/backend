from django.core.management.base import BaseCommand

from library.models import Author


class Command(BaseCommand):
    help = 'Create authors to test'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        # Author.objects.all().delete()
        count = options['count']
        for i in range(count):
            author = Author.objects.create(first_name=f'fname{i}',
                                           last_name=f'lname{i}',
                                           birthday_year=1700 + i)
            print(f'author {author.first_name} created')
        print('done')
