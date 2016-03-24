# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_settings', '0002_remove_review_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='published_date',
        ),
    ]
