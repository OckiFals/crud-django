# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0010_auto_20150125_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='foto',
            field=models.CharField(max_length=60, blank=True),
            preserve_default=True,
        ),
    ]
