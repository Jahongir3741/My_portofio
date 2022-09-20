# Generated by Django 4.1.1 on 2022-09-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=512)),
                ('your_email', models.EmailField(max_length=128, unique=True)),
                ('subject', models.CharField(max_length=512)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Networks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_link', models.URLField(max_length=256)),
                ('icon', models.CharField(max_length=64)),
            ],
        ),
    ]
