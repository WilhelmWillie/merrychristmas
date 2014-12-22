# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardcreator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='slug',
            field=models.CharField(default='00000', max_length=5),
            preserve_default=False,
        ),
    ]
