from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from time import gmtime, strftime
from .models import Twitter_user
from django.core import serializers
import json
from tweet_grabber import TwitterDataSheet

# HOME *************************************************


def index(request):
    if 'twtr_user' not in request.session:
        request.session['twtr_user'] = 'ryost_esq'
    else:
        context = {
            'user': Twitter_user.objects.get(
                screen_name=request.session['twtr_user']
            )
        }
    return render(request, 'index.html', context)


def grab(request):
    if request.method == 'POST':
        try:
            print request.session['twtr_user']
            user = Twitter_user.objects.get(screen_name=request.POST['screen_name'])
        except Twitter_user.DoesNotExist:
            print "not in Db"
            user = TwitterDataSheet(screen_name=request.POST['screen_name']).user
            Twitter_user.objects.create(user_id=user.id, name=user.name, screen_name=user.screen_name, location=user.location, url=user.url, friends_count=user.friends_count, followers_count=user.followers_count, email=user.email, description=user.description, user_since=user.created_at, time_zone=user.time_zone)
            request.session['twtr_user'] = request.POST['screen_name']    
        return redirect('in')
