# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20141202_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.ManyToManyField(to='core.Category'),
            preserve_default=True,
        ),
    ]
