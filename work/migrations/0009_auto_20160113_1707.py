# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0008_company_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_publicated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interview',
            name='is_publicated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='is_publicated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='size',
            field=models.CharField(default=b'7', max_length=1, choices=[(b'1', b'1-50'), (b'2', b'51-200'), (b'3', b'201-500'), (b'4', b'501-1000'), (b'5', b'1001-5000'), (b'6', b'> 5000'), (b'7', b'\xd0\x9d\xd0\xb5\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xb5\xd1\x81\xd1\x82\xd0\xbd\xd0\xbe')]),
        ),
    ]
