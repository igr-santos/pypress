# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20141110_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(unique=True, max_length=165)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(null=True, editable=False, blank=True)),
                ('status', models.CharField(default=b'D', max_length=1, editable=False, choices=[(b'D', b'Draft'), (b'P', b'Published'), (b'A', b'Approved')])),
                ('author', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='core.TagEntry', through='core.TaggedWhatever', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
