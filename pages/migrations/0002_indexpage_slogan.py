# Generated by Django 4.0.5 on 2022-07-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='slogan',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
