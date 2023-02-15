from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
now = timezone.now()

class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"
    FAILED = 'fail', "Deadline"


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=10, choices=Status.choices)
    start_date = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))

    def is_end_date(self):
        return now > self.due_date

    def __str__(self):
        return self.name
