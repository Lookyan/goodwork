# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from goodwork.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from work.models import Company


def home(request):
    return render(request, 'main.html', {})


def jobs(request):
    return render(request, 'jobs.html', {})


def job(request, job_id):
    return render(request, 'job.html', {})


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'signin.html', {'error': '2'})
        else:
            return render(request, 'signin.html', {'error': '1'})
    else:
        return render(request, 'signin.html', {})


def signup(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['username'] = str(int(User.objects.latest('id').id) + 1)  # race condition!
        form = SignUpForm(data)
        if form.is_valid():
            user = form.save()
            return render(request, 'main.html', {})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def settings(request):
    return render(request, 'settings.html', {})


@login_required
def add(request):
    if request.method == 'GET':
        return render(request, 'add.html', {})
    elif request.method == 'POST':
        type = request.POST['type']
        if type == 'review':
            return render(request, 'add-review.html', {})


def companyjs(request):
    term = request.GET['term']
    if len(term) < 3:
        return HttpResponseBadRequest()
    data = Company.objects.get_by_name_part(term)
    return JsonResponse(data, safe=False)