# Generated by Django 3.2.8 on 2021-12-06 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='categories',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]
