# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_userpostcomment_acces'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpostcomment',
            name='acces',
        ),
        migrations.AddField(
            model_name='post',
            name='acces',
            field=models.BooleanField(default=True),
        ),
    ]
