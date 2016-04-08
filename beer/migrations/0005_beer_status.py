# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    operations = [
        migrations.AddField(
            model_name='beer',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Available'), (2, b'Empty')]),
            preserve_default=True,
        ),
    ]
