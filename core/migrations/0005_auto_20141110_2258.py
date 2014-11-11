# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20141107_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created_at', '-published_at'], 'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(default=b'D', max_length=1, editable=False, choices=[(b'D', b'Draft'), (b'P', b'Published'), (b'A', b'Approved')]),
            preserve_default=True,
        ),
    ]
