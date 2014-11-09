# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20141107_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='draft',
        ),
        migrations.AddField(
            model_name='entry',
            name='status',
            field=models.CharField(default=b'D', max_length=1, choices=[(b'D', b'Draft'), (b'P', b'Published'), (b'A', b'Approved')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.CharField(unique=True, max_length=165),
            preserve_default=True,
        ),
    ]
