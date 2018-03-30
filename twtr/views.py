import os

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Twitter_user
from tweet_grabber import TwitterDataSheet, build_csv
from twitter.error import TwitterError


# HOME *************************************************
def index(request):
    if 'twtr_user' not in request.session:
        request.session['twtr_user'] = 'ryost_esq'
        root = os.getcwd()
        csv_path = "{}/twtr/static/csv/".format(root)
        request.session["csv_path"] = csv_path
    context = {
        'user': Twitter_user.objects.get(
            screen_name=request.session['twtr_user']
        )
    }
    return render(request, 'index.html', context)


# GRAB DATA FROM DATABASE/API ******************************************
def grab(request):
    if request.method == 'POST':
        try:
            root = os.getcwd()
            csv_path = "{}/twtr/static/csv/".format(root)

            user = Twitter_user.objects.get(
                screen_name=request.POST['screen_name']
            )

            user_csv = "{}.csv".format(
                request.POST['screen_name']
            )
            if user_csv not in os.listdir(csv_path):
                build_csv(request.POST['screen_name'])
        except Twitter_user.DoesNotExist:
            try:
                user = TwitterDataSheet(
                    screen_name=request.POST['screen_name']).user
                if not user.coordinates:
                    user.coordinates = (None, None)
                Twitter_user.objects.create(
                    user_id=user.id, name=user.name,
                    screen_name=user.screen_name, location=user.location,
                    url=user.url, friends_count=user.friends_count,
                    followers_count=user.followers_count, email=user.email,
                    description=user.description, user_since=user.created_at,
                    time_zone=user.time_zone, latitude=user.coordinates[0],
                    longitude=user.coordinates[1],
                    profile_img=user.profile_image_url
                )
                root = os.getcwd()
                csv_path = "{}/twtr/static/csv/".format(root)
                if user_csv not in os.listdir(csv_path):
                    build_csv(request.POST['screen_name'])
            except TwitterError:
                messages.error(request, "Twitter user does not exist")
                return redirect('in')
        request.session['twtr_user'] = request.POST['screen_name']
        return redirect('in')
