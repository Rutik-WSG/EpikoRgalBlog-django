# Generated by Django 4.1.2 on 2022-11-28 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('header', models.CharField(max_length=12)),
                ('img', models.ImageField(upload_to='')),
                ('short_description', models.CharField(max_length=50)),
                ('Aartical', models.CharField(max_length=20)),
            ],
        ),
    ]
