# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('to_recepient', models.CharField(max_length=36)),
                ('from_sender', models.CharField(max_length=36)),
                ('message', models.CharField(max_length=560)),
                ('img', models.CharField(max_length=36)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
