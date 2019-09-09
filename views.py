# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Ms. Lang. We're going to get these kids spelling.")

# Create your views here.
