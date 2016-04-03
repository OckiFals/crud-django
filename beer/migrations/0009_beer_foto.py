# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0008_auto_20150123_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='foto',
            field=models.CharField(default=b'beer-default.jpg', max_length=60),
            preserve_default=True,
        ),
    ]
