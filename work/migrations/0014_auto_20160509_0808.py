# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0013_interview_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='founded',
            field=models.PositiveSmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='revenue',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
