# Generated by Django 5.1.5 on 2025-03-29 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_rename_num_rooms_room_total_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='total_rooms',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
