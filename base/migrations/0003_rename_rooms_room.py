# Generated by Django 5.1 on 2024-08-18 08:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_rename_room_status_rooms_room_name_rooms_host_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rooms',
            new_name='Room',
        ),
    ]
