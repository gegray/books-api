# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('pubdate', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=2000)),
                ('price', models.FloatField()),
                ('url', models.URLField(max_length=2000)),
                ('coverimg', models.URLField(max_length=2000)),
            ],
        ),
    ]
