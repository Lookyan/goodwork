from django.contrib import admin
from .models import Company, Category, Job, City, Review, Salary, Interview, InterviewQuestion, JobType


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    pass


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass


@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    pass