# Generated by Django 5.0.4 on 2024-04-30 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_rename_animal_prize_animal_animal_prize_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='animal_farm',
            new_name='Animal_Farm',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='User',
            new_name='user',
        ),
    ]
