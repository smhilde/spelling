# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Week, Word

# Register your models here.
admin.site.register(Week)
admin.site.register(Word)
