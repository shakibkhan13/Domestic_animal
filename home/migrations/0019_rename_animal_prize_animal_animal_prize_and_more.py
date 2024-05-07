# Generated by Django 5.0.4 on 2024-04-30 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_rename_animal_color_animal_animal_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='animal_prize',
            new_name='Animal_Prize',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='animal_weight',
            new_name='Animal_Weight',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='animal_color',
            new_name='Animal_color',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='animal_description',
            new_name='Animal_description',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='animal_image',
            new_name='Animal_image',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='animal_name',
            new_name='Animal_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='Price',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
    ]