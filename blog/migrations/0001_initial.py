# Generated by Django 3.2.8 on 2021-12-04 20:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('poster_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=2500)),
                ('rating', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.book')),
            ],
        ),
    ]