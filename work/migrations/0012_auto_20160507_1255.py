# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0011_auto_20160114_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': '\u0413\u043e\u0440\u043e\u0434', 'verbose_name_plural': '\u0413\u043e\u0440\u043e\u0434\u0430'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': '\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f', 'verbose_name_plural': '\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='interview',
            options={'verbose_name': '\u0421\u043e\u0431\u0435\u0441\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435', 'verbose_name_plural': '\u0421\u043e\u0431\u0435\u0441\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='interviewquestion',
            options={'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441 \u043d\u0430 \u0438\u043d\u0442\u0435\u0440\u0432\u044c\u044e', 'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b \u043d\u0430 \u0438\u043d\u0442\u0435\u0440\u0432\u044c\u044e'},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': '\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u044f', 'verbose_name_plural': '\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='jobtype',
            options={'verbose_name': '\u041f\u043e\u0437\u0438\u0446\u0438\u044f', 'verbose_name_plural': '\u041f\u043e\u0437\u0438\u0446\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': '\u041e\u0442\u0437\u044b\u0432', 'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432\u044b'},
        ),
        migrations.AlterModelOptions(
            name='salary',
            options={'verbose_name': '\u0417\u0430\u0440\u043f\u043b\u0430\u0442\u0430', 'verbose_name_plural': '\u0417\u0430\u0440\u043f\u043b\u0430\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xd0\x92\xd0\xb5\xd0\xb1-\xd1\x81\xd0\xb0\xd0\xb9\xd1\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='job',
            field=models.ForeignKey(to='work.JobType'),
        ),
    ]
