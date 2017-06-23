# -*- coding: utf-8 -*-
#pylint: disable=C0111
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    # User.objects.all().delete
    return render(request, 'login/index.html')

def register(request):
    results = User.objects.registervalidate(request.POST)
    print "***UserResult, back in views ***", newuser['status']
    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        messages.success(request, "User was created, please login.")
    return redirect('/')

def login(request):
    results = User.objects.loginvalidate(request.POST)
    if results['status'] is False:
        messages.error(request, 'Please check your login and try again...')
        return redirect('/')
    # request.session['userid'] = results['user'].id
    # request.session['first_name'] = results['user'].first_name
    # request.session['last_name'] = results['user'].last_name
    return redirect('/mainpage')

def logout(request):
    request.session.all().flush()

def mainpage(request):
    return render(request, 'login/mainpage.html')
