from django.core.management.base import BaseCommand
from faker import Faker
from tasks.models import *
import random
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()

        priorities = Priority.objects.all()
        categories = Category.objects.all()

        for _ in range(30):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(elements=["Pending","In Progress","Completed"]),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                priority=random.choice(priorities),
                category=random.choice(categories)
            )

            for _ in range(3):
                SubTask.objects.create(
                    parent_task=task,
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(elements=["Pending","In Progress","Completed"])
                )

            Note.objects.create(
                task=task,
                content=fake.paragraph(nb_sentences=2)
            )

        self.stdout.write(self.style.SUCCESS("Fake data generated!"))