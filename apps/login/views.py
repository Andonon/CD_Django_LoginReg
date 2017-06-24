# -*- coding: utf-8 -*-
#pylint: disable=C0111
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    # testdelete = User.objects.all().delete()
    return render(request, 'login/index.html')

def register(request):
    results = User.objects.registervalidate(request.POST)
    print "***UserResult, back in views ***", results['status']
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
        messages.error(request, 'Login failed.')
        return redirect('/')
    else:
        print results['user'], "1"*50
        user = User.objects.get(id=results['user'])
        print user.id, "4"*50
        request.session['userid'] = user.id
        print "Just set session userid: ", request.session['userid'], "*"*50
        request.session['first_name'] = user.first_name
        print "Just set session first_name: ", request.session['first_name'], "*"*50
        request.session['last_name'] = user.last_name
        print "Just set session last_name: ", request.session['last_name'], "*"*50
    return redirect('/mainpage')

def logout(request):
    flushcookie = request.session.flush()
    return redirect('/')

def mainpage(request):
    try:
        request.session['userid']
    except KeyError:
        flushcookie = request.session.flush()
        messages.error(request, 'Oh Snap! There is no session cookie detected, please login.')
        return redirect('/')
    return render(request, 'login/mainpage.html')
