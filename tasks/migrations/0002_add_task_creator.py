# Generated by Django 4.1.6 on 2023-02-15 04:19
from django.conf import settings
from django.db import migrations, models
from django.template.backends import django
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(model_name='Task', name='creator',
                            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks',
                                                    to=settings.AUTH_USER_MODEL, null=True))
    ]
