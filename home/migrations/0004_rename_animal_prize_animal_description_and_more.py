# Generated by Django 5.0.3 on 2024-03-20 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_animal_animal_prize'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='Animal_Prize',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='Animal_Weight',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='Animal_Farm',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='Animal_description',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='Animal_image',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='Animal_name',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='Animal_view_count',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='user',
        ),
        migrations.AddField(
            model_name='animal',
            name='farm',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.ImageField(default='https://via.placeholder.com/150', upload_to='animal_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='prize',
            field=models.DecimalField(decimal_places=2, default='10.00', max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=50.0, max_digits=5),
            preserve_default=False,
        ),
    ]
