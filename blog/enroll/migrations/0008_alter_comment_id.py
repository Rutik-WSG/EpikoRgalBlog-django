# Generated by Django 4.1.3 on 2022-11-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0007_comment_delete_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
