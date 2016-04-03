# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinker', '0002_auto_20150109_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinker',
            name='birthday',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
