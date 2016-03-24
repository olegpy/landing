# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainSlider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'static/img/uploads/%Y/%m/%d/')),
                ('header', models.CharField(max_length=25, blank=True)),
                ('description', models.TextField(blank=True)),
                ('btn_text', models.CharField(max_length=10, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'static/img/uploads/%Y/%m/%d/')),
                ('url_video', models.CharField(max_length=25, blank=True)),
                ('author', models.CharField(max_length=25, blank=True)),
                ('header', models.CharField(max_length=25, blank=True)),
                ('description', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to=b'static/img/uploads/%Y/%m/%d/')),
                ('description', models.TextField()),
            ],
        ),
    ]
