# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 03:19
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(blank=True, max_length=200, null=True)),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sexo', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], max_length=1)),
                ('sobre_mi', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Autores',
                'verbose_name': 'Autor',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Profesiones',
                'verbose_name': 'Profesion',
            },
        ),
        migrations.AddField(
            model_name='autor',
            name='profesion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlog.Profesion'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlog.Categoria'),
        ),
    ]
