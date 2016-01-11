# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('icon', models.ImageField(upload_to=b'categories')),
                ('parent', models.ForeignKey(to='work.Category')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to=b'companies')),
                ('size', models.IntegerField(default=0)),
                ('engaged', models.BooleanField(default=False)),
                ('founded', models.PositiveSmallIntegerField(default=0)),
                ('revenue', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('experience', models.CharField(default=b'+', max_length=1, choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Neutral')])),
                ('description', models.TextField()),
                ('difficulty', models.CharField(default=b'NC', max_length=2, choices=[(b'VE', b'Very easy'), (b'E', b'Easy'), (b'A', b'Average'), (b'D', b'Difficult'), (b'VD', b'Very difficult'), (b'NC', b'Not Checked')])),
                ('offer', models.CharField(default=b'NC', max_length=1, choices=[(b'Y', b'Yes'), (b'D', b'Declined'), (b'N', b'No'), (b'NC', b'Not Checked')])),
                ('entire_process', models.PositiveSmallIntegerField(default=0)),
                ('duration', models.CharField(default=b'D', max_length=1, choices=[(b'D', b'Days'), (b'W', b'Weeks'), (b'M', b'Months')])),
                ('place', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('experience', models.PositiveSmallIntegerField(default=0)),
                ('type', models.CharField(default=b'FT', max_length=2, choices=[(b'FT', b'Full Time'), (b'PT', b'Part Time'), (b'CT', b'Contract'), (b'IS', b'Internship'), (b'TY', b'Temporary'), (b'EL', b'Entry Level'), (b'NC', b'Not checked')])),
                ('category', models.ForeignKey(to='work.Category')),
                ('company', models.ForeignKey(to='work.Company')),
                ('location', models.ForeignKey(to='work.City')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('is_current_employee', models.BooleanField(default=False)),
                ('status', models.CharField(default=b'NC', max_length=2, choices=[(b'FT', b'Full Time'), (b'PT', b'Part Time'), (b'CT', b'Contract'), (b'IN', b'Intern'), (b'FL', b'Freelance'), (b'NC', b'Not Checked')])),
                ('title', models.CharField(max_length=200)),
                ('pros', models.TextField()),
                ('cons', models.TextField()),
                ('company', models.ForeignKey(to='work.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(default=0)),
                ('experience', models.PositiveSmallIntegerField(default=0)),
                ('status', models.CharField(default=b'NC', max_length=2, choices=[(b'FT', b'Full Time'), (b'PT', b'Part Time'), (b'CT', b'Contract'), (b'IN', b'Intern'), (b'FL', b'Freelance'), (b'NC', b'Not Checked')])),
                ('company', models.ForeignKey(to='work.Company')),
                ('job', models.ForeignKey(to='work.Job')),
                ('location', models.ForeignKey(to='work.City')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='group',
            field=models.CharField(default=b'RU', max_length=2, choices=[(b'RU', b'Regular User'), (b'MO', b'Moderator')]),
        ),
        migrations.AddField(
            model_name='interview',
            name='job',
            field=models.ForeignKey(to='work.Job'),
        ),
        migrations.AddField(
            model_name='interview',
            name='question',
            field=models.ManyToManyField(to='work.InterviewQuestion'),
        ),
    ]
