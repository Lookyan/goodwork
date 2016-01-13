# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from managers import CompanyManager


class Profile(models.Model):
    user = models.OneToOneField(User)
    REGULAR_USER = 'RU'
    MODERATOR = 'MO'

    TYPE_OF_USER_CHOICES = (
        (REGULAR_USER, 'Regular User'),
        (MODERATOR, 'Moderator'),
    )
    group = models.CharField(max_length=2,
                             choices=TYPE_OF_USER_CHOICES,
                             default=REGULAR_USER)


class Company(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='companies', default=None, null=True, blank=True)

    EMP1_50 = '1'
    EMP51_200 = '2'
    EMP201_500 = '3'
    EMP501_1000 = '4'
    EMP1001_5000 = '5'
    EMPGT5000 = '6'
    UNKNOWN = '7'

    SIZE_EMPS_CHOICES = (
        (EMP1_50, '1-50'),
        (EMP51_200, '51-200'),
        (EMP201_500, '201-500'),
        (EMP501_1000, '501-1000'),
        (EMP1001_5000, '1001-5000'),
        (EMPGT5000, '> 5000'),
        (UNKNOWN, 'Неизвестно'),
    )
    size = models.CharField(max_length=1,
                            choices=SIZE_EMPS_CHOICES,
                            default=UNKNOWN)
    engaged = models.BooleanField(default=False)
    founded = models.PositiveSmallIntegerField(default=0)
    revenue = models.IntegerField(default=0)
    description = models.TextField()
    is_publicated = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    objects = CompanyManager()


class Job(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey('Company')
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    location = models.ForeignKey('City', default=None, null=True, blank=True)
    experience = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey('Category')
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    CONTRACT = 'CT'
    INTERNSHIP = 'IS'
    TEMPORARY = 'TY'
    ENTRY_LEVEL = 'EL'
    NOT_CHECKED = 'NC'

    TYPE_OF_JOB_CHOICES = (
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (CONTRACT, 'Contract'),
        (INTERNSHIP, 'Internship'),
        (TEMPORARY, 'Temporary'),
        (ENTRY_LEVEL, 'Entry Level'),
        (NOT_CHECKED, 'Not checked'),
    )
    type = models.CharField(max_length=2,
                            choices=TYPE_OF_JOB_CHOICES,
                            default=FULL_TIME)


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('Category', default=None, null=True, blank=True)
    icon = models.ImageField(upload_to='categories', default=None, null=True, blank=True)


class City(models.Model):
    name = models.CharField(max_length=50)


class Review(models.Model):
    user = models.ForeignKey(User, default=None)
    company = models.ForeignKey(Company)
    is_publicated = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(default=0)
    is_current_employee = models.BooleanField(default=False)
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    CONTRACT = 'CT'
    INTERN = 'IN'
    FREELANCE = 'FL'
    NOT_CHECKED = 'NC'

    EMPLOYMENT_STATUS = (
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (CONTRACT, 'Contract'),
        (INTERN, 'Intern'),
        (FREELANCE, 'Freelance'),
        (NOT_CHECKED, 'Not Checked'),
    )
    status = models.CharField(max_length=2,
                              choices=EMPLOYMENT_STATUS,
                              default=NOT_CHECKED)
    title = models.CharField(max_length=200, default=None, null=True, blank=True)
    pros = models.TextField()
    cons = models.TextField()


class Salary(models.Model):
    user = models.ForeignKey(User, default=None)
    job = models.ForeignKey('Job')
    company = models.ForeignKey('Company')
    value = models.IntegerField(default=0)
    experience = models.PositiveSmallIntegerField(default=0)
    location = models.ForeignKey('City', default=None, null=True, blank=True)
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    CONTRACT = 'CT'
    INTERN = 'IN'
    FREELANCE = 'FL'
    NOT_CHECKED = 'NC'

    EMPLOYMENT_STATUS = (
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (CONTRACT, 'Contract'),
        (INTERN, 'Intern'),
        (FREELANCE, 'Freelance'),
        (NOT_CHECKED, 'Not Checked'),
    )
    status = models.CharField(max_length=2,
                              choices=EMPLOYMENT_STATUS,
                              default=NOT_CHECKED)


class Interview(models.Model):
    user = models.ForeignKey(User, default=None)
    POSITIVE = '+'
    NEGATIVE = '-'
    NEUTRAL = '?'

    TYPE_EXPERIENCE = (
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative'),
        (NEUTRAL, 'Neutral')
    )
    experience = models.CharField(max_length=1,
                                  choices=TYPE_EXPERIENCE,
                                  default=POSITIVE)
    job = models.ForeignKey('Job')
    description = models.TextField()
    question = models.ManyToManyField('InterviewQuestion')
    is_publicated = models.BooleanField(default=False)
    VERY_EASY = 'VE'
    EASY = 'E'
    AVERAGE = 'A'
    DIFFICULT = 'D'
    VERY_DIFFICULT = 'VD'
    NOT_CHECKED = 'NC'

    TYPE_DIFFICULTY = (
        (VERY_EASY, 'Very easy'),
        (EASY, 'Easy'),
        (AVERAGE, 'Average'),
        (DIFFICULT, 'Difficult'),
        (VERY_DIFFICULT, 'Very difficult'),
        (NOT_CHECKED, 'Not Checked'),
    )
    difficulty = models.CharField(max_length=2,
                                  choices=TYPE_DIFFICULTY,
                                  default=NOT_CHECKED)
    YES = 'Y'
    DECLINED = 'D'
    NO = 'N'

    TYPE_OFFER = (
        (YES, 'Yes'),
        (DECLINED, 'Declined'),
        (NO, 'No'),
        (NOT_CHECKED, 'Not Checked'),
    )
    offer = models.CharField(max_length=1,
                             choices=TYPE_OFFER,
                             default=NOT_CHECKED)
    entire_process = models.PositiveSmallIntegerField(default=0)
    DAYS = 'D'
    WEEKS = 'W'
    MONTHS = 'M'

    DURATION_IN = (
        (DAYS, 'Days'),
        (WEEKS, 'Weeks'),
        (MONTHS, 'Months'),
    )
    duration = models.CharField(max_length=1,
                                choices=DURATION_IN,
                                default=DAYS)
    place = models.CharField(max_length=250)


class InterviewQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
