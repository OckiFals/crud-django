# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0003_mahasiswa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='mahasiswa',
        ),
    ]
