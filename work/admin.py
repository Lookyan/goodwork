from django.contrib import admin
from .models import Company, Category, Job, City, Review, Salary, Interview, InterviewQuestion, JobType


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    list_per_page = 20
    list_filter = ('size', 'is_publicated')
    search_fields = ('name',)


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
    list_per_page = 20
    list_filter = ('is_publicated', 'rating', 'status')
    search_fields = ('title',)


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    pass


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ('is_publicated', 'experience', 'difficulty', 'offer')


@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    pass