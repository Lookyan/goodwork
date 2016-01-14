# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0010_auto_20160114_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='salary',
            name='experience',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, b'\xd0\x9c\xd0\xb5\xd0\xbd\xd1\x8c\xd1\x88\xd0\xb5 \xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb0'), (1, b'\xd0\x9e\xd0\xb4\xd0\xb8\xd0\xbd \xd0\xb3\xd0\xbe\xd0\xb4'), (2, b'\xd0\x94\xd0\xb2\xd0\xb0 \xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb0'), (3, b'3-5 \xd0\xbb\xd0\xb5\xd1\x82'), (6, b'6-10 \xd0\xbb\xd0\xb5\xd1\x82'), (10, b'\xd0\x91\xd0\xbe\xd0\xbb\xd1\x8c\xd1\x88\xd0\xb5 10 \xd0\xbb\xd0\xb5\xd1\x82')]),
        ),
        migrations.AlterField(
            model_name='salary',
            name='job',
            field=models.ForeignKey(to='work.JobType'),
        ),
    ]
