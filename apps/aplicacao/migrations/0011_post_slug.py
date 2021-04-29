# Generated by Django 3.1.7 on 2021-04-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0010_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True, verbose_name='Atalho'),
            preserve_default=False,
        ),
    ]
