# Generated by Django 5.0.4 on 2024-04-30 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_animal_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='Animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.animal'),
        ),
    ]
