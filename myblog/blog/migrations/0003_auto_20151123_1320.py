# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
