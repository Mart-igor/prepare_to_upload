# Generated by Django 5.1.4 on 2024-12-11 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_celestial_stripe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celestial',
            name='stripe_id',
        ),
    ]
