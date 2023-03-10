# Generated by Django 4.1.7 on 2023-02-20 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, null=True)),
                ('litle_text', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(max_length=10000, null=True)),
            ],
            options={
                'verbose_name': 'О кинотеатре',
                'verbose_name_plural': 'О кинотеатре',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('subject', models.CharField(max_length=222)),
                ('text', models.TextField(max_length=3333)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, null=True)),
                ('text', models.CharField(max_length=555, null=True)),
            ],
            options={
                'verbose_name': 'Наши партнеры',
                'verbose_name_plural': 'Наши партнеры',
            },
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('litle_text', models.CharField(max_length=350, null=True)),
                ('text_1', models.TextField(max_length=10000, null=True)),
                ('text_2', models.TextField(max_length=10000, null=True)),
                ('text_3', models.TextField(max_length=10000, null=True)),
                ('text_4', models.TextField(max_length=10000, null=True)),
                ('text_5', models.TextField(max_length=10000, null=True)),
            ],
            options={
                'verbose_name': 'Политика конфиденциальности',
                'verbose_name_plural': 'Политика конфиденциальности',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, null=True)),
                ('litle_title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=555, null=True)),
                ('bg', models.FileField(upload_to='bg/')),
                ('logo', models.FileField(upload_to='logo/')),
                ('phone', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('graphic', models.CharField(max_length=50, null=True)),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('tiktok', models.URLField()),
                ('twitter', models.URLField()),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
        migrations.CreateModel(
            name='PartnersImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.URLField()),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='settings.partners')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='settings.about')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
    ]
