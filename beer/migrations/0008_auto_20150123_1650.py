# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0007_auto_20150123_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beer',
            name='status',
        ),
        migrations.AlterField(
            model_name='beer',
            name='price',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beer',
            name='stock',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
