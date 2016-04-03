# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinker', '0004_drinker_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinker',
            name='foto',
        ),
    ]
