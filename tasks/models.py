from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
now = timezone.now()


class Status(models.TextChoices):
    STARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"
    FAILED = 'fail', "Failed"


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=100, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=10, choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
