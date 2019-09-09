# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Week(models.Model):
    week_number = models.IntegerField()

    def __str__(self):
        return "week_number={}".format(self.week_number)

class Word(models.Model):
    spelling_word = models.CharField(max_length=25)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    grade_level = models.IntegerField()

    def __str__(self):
        return "spelling_word={}, grade_level={}, week={}".format(self.spelling_word,
                                                                  self.grade_level,
                                                                  self.week)
