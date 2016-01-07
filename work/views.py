# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


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
        user = authenticate(email=email, password=password)
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
    return render(request, 'signup.html', {})