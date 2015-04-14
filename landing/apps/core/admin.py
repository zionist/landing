from django.contrib import admin

from landing.apps.core.models import LandingPage, Block
# Register your models here.

admin.site.register(LandingPage)
admin.site.register(Block)