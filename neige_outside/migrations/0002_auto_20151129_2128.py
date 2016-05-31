# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neige_outside', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.CharField(default='sample', max_length=104),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=10000),
        ),
    ]
