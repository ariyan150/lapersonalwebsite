# Generated by Django 2.1.5 on 2020-12-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.TextField(null=True),
        ),
    ]
