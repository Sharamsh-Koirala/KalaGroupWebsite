# Generated by Django 4.0.5 on 2022-10-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='ending_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]