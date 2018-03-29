from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from time import gmtime, strftime
from .models import *
from django.core import serializers
import json

# HOME *************************************************

def index(request):
    return render(request, 'index.html')
