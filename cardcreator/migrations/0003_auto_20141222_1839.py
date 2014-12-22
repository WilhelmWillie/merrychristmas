# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardcreator', '0002_card_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='to_recepient',
            new_name='to_recipient',
        ),
    ]
