# Generated by Django 3.1.7 on 2021-04-29 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0009_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
