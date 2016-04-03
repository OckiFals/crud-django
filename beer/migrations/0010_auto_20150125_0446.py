# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0009_beer_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='foto',
            field=models.CharField(default=b'beer-default.jpg', max_length=60, blank=True),
            preserve_default=True,
        ),
    ]
