from django.db import models
from django.contrib.auth.models import User


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
    logo = models.ImageField(upload_to='companies')
    size = models.IntegerField(default=0)
    engaged = models.BooleanField(default=False)
    founded = models.PositiveSmallIntegerField(default=0)
    revenue = models.IntegerField(default=0)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)


class Job(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey('Company')
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    location = models.ForeignKey('City')
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
    parent = models.ForeignKey('Category')
    icon = models.ImageField(upload_to='categories')


class City(models.Model):
    name = models.CharField(max_length=50)


class Review(models.Model):
    company = models.ForeignKey(Company)
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
    title = models.CharField(max_length=200)
    pros = models.TextField()
    cons = models.TextField()


class Salary(models.Model):
    job = models.ForeignKey('Job')
    company = models.ForeignKey('Company')
    value = models.IntegerField(default=0)
    experience = models.PositiveSmallIntegerField(default=0)
    location = models.ForeignKey('City')
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
