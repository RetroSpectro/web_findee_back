# Generated by Django 2.2.7 on 2019-12-03 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20191203_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='profile_images/%Y/%m/%d', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.Profile', verbose_name='Профиль'),
        ),
    ]
