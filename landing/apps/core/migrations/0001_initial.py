# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('header', models.CharField(verbose_name='header', max_length=512)),
                ('content', models.CharField(verbose_name='content', max_length=1024)),
                ('block_image', models.ImageField(upload_to='', verbose_name='block_image')),
            ],
        ),
        migrations.CreateModel(
            name='EmailSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('to', models.EmailField(verbose_name='to', max_length=1024)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('header', models.CharField(verbose_name='header', max_length=2048)),
                ('content', models.TextField(verbose_name='content')),
                ('contacts', models.CharField(verbose_name='contacts', max_length=2048)),
                ('logo', models.ImageField(upload_to='', verbose_name='logo')),
                ('background', models.ImageField(upload_to='', verbose_name='background')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='landing_page',
            field=models.ForeignKey(to='core.LandingPage'),
        ),
    ]
