# Generated by Django 4.2.6 on 2023-11-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(upload_to='img/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_for_cooking',
            field=models.IntegerField(default=10),
        ),
    ]