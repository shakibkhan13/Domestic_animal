# Generated by Django 5.0.3 on 2024-03-20 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_animal_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='farm',
            new_name='Animal_Farm',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='prize',
            new_name='Animal_Prize',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='weight',
            new_name='Animal_Weight',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='description',
            new_name='Animal_description',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='image',
            new_name='Animal_image',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='name',
            new_name='Animal_name',
        ),
    ]
