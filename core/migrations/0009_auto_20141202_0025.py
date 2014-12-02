# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20141202_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(unique=True, max_length=165),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(unique=True, max_length=165),
            preserve_default=True,
        ),
    ]
