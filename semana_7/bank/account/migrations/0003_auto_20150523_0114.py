# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150503_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
