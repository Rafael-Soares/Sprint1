# Generated by Django 3.1.7 on 2021-04-27 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0007_auto_20210426_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientesparceiros',
            name='image_Parceiro',
            field=models.FileField(blank=True, upload_to='imagens_SVG/', verbose_name='Imagem do parceiro'),
        ),
    ]
