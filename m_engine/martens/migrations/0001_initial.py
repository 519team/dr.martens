# Generated by Django 3.0.8 on 2020-07-21 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProdPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FilePathField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('location', models.CharField(max_length=20)),
                ('segment', models.CharField(max_length=20)),
                ('overall_rating', models.FloatField()),
                ('pros', models.TextField(blank=True)),
                ('cons', models.TextField(blank=True)),
                ('confirmed', models.DateField()),
                ('published', models.DateField()),
                ('helpful', models.CharField(blank=True, max_length=10)),
                ('photo_path', models.FilePathField(null=True)),
            ],
        ),
    ]
