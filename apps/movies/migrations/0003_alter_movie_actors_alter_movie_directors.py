# Generated by Django 4.1.7 on 2023-02-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_actors_alter_movie_directors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(blank=True, max_length=50000, null=True, verbose_name='Актёры'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.CharField(max_length=555, verbose_name='Режиссёры'),
        ),
    ]