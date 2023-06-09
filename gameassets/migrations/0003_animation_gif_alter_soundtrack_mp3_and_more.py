# Generated by Django 4.2.1 on 2023-05-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameassets', '0002_remove_animation_gif'),
    ]

    operations = [
        migrations.AddField(
            model_name='animation',
            name='gif',
            field=models.FilePathField(null=True, path='/gameassets/gif'),
        ),
        migrations.AlterField(
            model_name='soundtrack',
            name='mp3',
            field=models.FilePathField(null=True, path='/gameassets/mp3'),
        ),
        migrations.AlterField(
            model_name='sprite',
            name='image',
            field=models.FilePathField(null=True, path='/gameassets/img'),
        ),
    ]
