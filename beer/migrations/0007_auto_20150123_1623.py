# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0006_auto_20150114_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='price',
            field=models.FloatField(default=125000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beer',
            name='stock',
            field=models.IntegerField(default=40),
            preserve_default=True,
        ),
    ]
