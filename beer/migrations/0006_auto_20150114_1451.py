# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0005_beer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='status',
            field=models.IntegerField(choices=[(1, b'Available'), (2, b'Empty')]),
            preserve_default=True,
        ),
    ]
