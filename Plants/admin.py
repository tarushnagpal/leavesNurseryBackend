# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Plants.models import Plant, Categories

admin.site.register(Plant)
admin.site.register(Categories)

# Register your models here.
