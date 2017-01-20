# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20161220_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='imagelink',
            field=models.CharField(default='No Image/Video', max_length=300),
        ),
    ]
