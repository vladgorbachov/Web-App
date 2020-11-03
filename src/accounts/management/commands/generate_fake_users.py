from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from faker import Faker
from django.conf import settings


f = Faker()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self,  *args, **options):
        group = Group(name=settings.ADMIN_GROUP)
        group.save()

        for _ in range(options["count"][0]):
            user = User(username=f.user_name(),
                        email=f.email(),
                        password=f.password())

            group.user_set.add(user)
        User.objects.bulk_create(user)


