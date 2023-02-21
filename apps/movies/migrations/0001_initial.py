# Generated by Django 4.1.7 on 2023-02-20 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('age', models.SmallIntegerField(default=0, verbose_name='Возраст')),
                ('image', models.FileField(upload_to='actors/')),
            ],
            options={
                'verbose_name': 'Актер',
                'verbose_name_plural': 'Актеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Понятный для')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('age', models.SmallIntegerField(default=0, verbose_name='Возраст')),
                ('image', models.FileField(upload_to='directors/')),
            ],
            options={
                'verbose_name': 'Режиссер',
                'verbose_name_plural': 'Режиссеры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название фильма')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Понятный для')),
                ('description', models.CharField(max_length=500, verbose_name='Описание фильма')),
                ('poster', models.ImageField(upload_to='movie_poster/', verbose_name='Постер фильма')),
                ('trailer', models.URLField(verbose_name='Трейлер')),
                ('movie', models.FileField(upload_to='movie_video/', verbose_name='Посмотреть фильм')),
                ('year', models.DateField(default=0, verbose_name='Дата выпуска')),
                ('running_time', models.CharField(max_length=10, verbose_name='Длительность фильма')),
                ('country', models.CharField(max_length=200, verbose_name='Страна')),
                ('genres', models.CharField(max_length=255, verbose_name='Жанры')),
                ('rating', models.FloatField(default=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('actors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.actor', verbose_name='актеры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Категории')),
                ('directors', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.directors', verbose_name='режиссеры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='movies.movie')),
            ],
            options={
                'verbose_name': 'Сериал',
                'verbose_name_plural': 'Сериалы',
            },
        ),
        migrations.CreateModel(
            name='Photomovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='movies.movie')),
            ],
            options={
                'verbose_name': 'Галерея фильмов',
                'verbose_name_plural': 'Галерея фильмов',
            },
        ),
    ]
