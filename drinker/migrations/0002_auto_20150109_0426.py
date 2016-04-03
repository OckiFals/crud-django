# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinker',
            name='birthday',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
    ]
