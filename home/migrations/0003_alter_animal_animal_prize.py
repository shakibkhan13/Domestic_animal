# Generated by Django 5.0.3 on 2024-03-19 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_animal_animal_farm_animal_animal_prize_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='Animal_Prize',
            field=models.TextField(),
        ),
    ]
