# Generated by Django 3.1.3 on 2020-11-25 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Task name')),
                ('status', models.CharField(
                    choices=[('u', 'Not started yet'), ('o', 'Ongoing'), ('f', 'Finished'), ('fail', 'Failed')],
                    max_length=10, verbose_name='Task status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
