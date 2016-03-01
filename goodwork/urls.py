"""goodwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'work.views.home', name='home'),
    url(r'^job/$', 'work.views.jobs', name='jobs'),
    url(r'^job/(\d*)', 'work.views.job', name='job'),
    url(r'^signin/$', 'work.views.signin', name='signin'),
    url(r'^signup/$', 'work.views.signup', name='signup'),
    url(r'^settings/$', 'work.views.settings', name='settings'),
    url(r'^add/$', 'work.views.add', name='add'),
    url(r'^add/review/$', 'work.views.add_review', name='add_review'),
    url(r'^add/salary/$', 'work.views.add_salary', name='add_salary'),
    url(r'^add/interview/$', 'work.views.add_interview', name='add_interview'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^companyjs/$', 'work.views.companyjs', name='companyjs'),
    url(r'^companycheck/$', 'work.views.company_check', name='company_check'),
    url(r'^companycreate/$', 'work.views.company_create_js', name='company_create_js'),
    url(r'^company/$', 'work.views.companies', name='companies'),
    url(r'^salary/$', 'work.views.salaries', name='salaries'),
    url(r'^interview/$', 'work.views.interviews', name='interviews'),
    url(r'^posjs/$', 'work.views.position_js', name='position_js'),
]
