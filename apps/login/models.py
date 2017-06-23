# -*- coding: utf-8 -*-
#pylint: disable=c0111
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def registervalidate(self, postdata):
        results = {'status':True, 'errors':[], 'user':None}
        if not postdata['first_name'] or len(postdata['first_name']) < 3:
            results['errors'].append("First name must be at least 3 characters")
            results['status'] = False
        if not postdata['last_name'] or len(postdata['last_name']) < 3:
            results['errors'].append("Last name must be at least 3 characters")
            results['status'] = False
        if not postdata['email'] or \
            not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postdata['email']):
            results['errors'].append("Email must be a valid email address")
            results['status'] = False
        if not postdata['password'] or len(postdata['password']) < 8:
            results['errors'].append("Password must be at least 8 characters")
            results['status'] = False
        if postdata['password'] != postdata['cpassword']:
            results['errors'].append("Passwords do not match")
            results['status'] = False
        user = User.objects.filter(email=postdata['email'])
        if user:
            results['status'] = False
            results['errors'].append("User already exists. Please login...")
        if results['status']:
            password = bcrypt.hashpw(postdata['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(
                first_name=postdata['first_name'],
                last_name=postdata['last_name'],
                email=postdata['email'],
                password=password)
            results['user'] = user
        return results

    def loginvalidate(self, postdata):
        results = {'status':True, 'errors':[], 'user':None}
        user = User.objects.filter(email = postdata['email'])
        print user[0]
        # user = User.objects.filter(email=postdata['email'])
        # userlen = len(user)
        # if userlen > 1:
        #     if user['password'] != \
        #     bcrypt.hashpw(postdata['password'].encode(), user['password'].encode()):
        #         results['status'] = False
        # else:
        #     results['user'] = user[0]    
        return results

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.email
    objects = UserManager()
