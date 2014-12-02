# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='extra',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='config',
            name='value',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
