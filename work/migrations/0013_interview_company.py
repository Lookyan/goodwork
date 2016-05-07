# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0012_auto_20160507_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='company',
            field=models.ForeignKey(default=None, to='work.Company'),
            preserve_default=False,
        ),
    ]
