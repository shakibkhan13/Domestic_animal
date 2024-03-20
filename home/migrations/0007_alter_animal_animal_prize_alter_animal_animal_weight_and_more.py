# Generated by Django 5.0.3 on 2024-03-20 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_farm_animal_animal_farm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='Animal_Prize',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='animal',
            name='Animal_Weight',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='animal',
            name='Animal_image',
            field=models.ImageField(default='', upload_to='animal_images'),
        ),
    ]