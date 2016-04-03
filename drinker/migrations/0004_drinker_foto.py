# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinker', '0003_auto_20150109_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinker',
            name='foto',
            field=models.CharField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
    ]
