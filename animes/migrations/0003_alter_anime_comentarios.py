# Generated by Django 4.0.5 on 2022-06-21 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0002_alter_anime_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='comentarios',
            field=models.CharField(blank=True, max_length=50, verbose_name='Comentários'),
        ),
    ]
