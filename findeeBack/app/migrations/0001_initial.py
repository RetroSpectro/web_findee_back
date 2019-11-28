# Generated by Django 2.2.7 on 2019-11-27 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Отчество')),
                ('kind', models.CharField(choices=[('specialist', 'Специалист'), ('client', 'Клиент')], max_length=20, verbose_name='Клиент или специалист')),
                ('regions', models.CharField(max_length=100, verbose_name='Регионы')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]