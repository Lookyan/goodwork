# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20160111_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(default=None, upload_to=b'categories'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(default=None, to='work.Category'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default=None, upload_to=b'companies'),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.ForeignKey(default=None, to='work.City'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='salary',
            name='location',
            field=models.ForeignKey(default=None, to='work.City'),
        ),
    ]
