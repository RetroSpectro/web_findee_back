# Generated by Django 2.2.7 on 2019-12-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20191201_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verify',
            field=models.BooleanField(default=False, verbose_name='Верифицирован'),
        ),
    ]
