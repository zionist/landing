from django.db import models
from django.utils.translation import ugettext as u
from django.contrib.auth.models import User


#def make_choises():
#    l = [];
#    for user in User.objects.using('default').all():
#        l.append((user, user))
#    return tuple(l)

class LandingPage(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, verbose_name=u('user'))
    header = models.CharField(max_length=2048, null=False, blank=False, verbose_name=u('header'))
    content = models.TextField(null=False, blank=False, verbose_name=u('content'))
    contacts = models.CharField(max_length=2048, null=False, blank=False, verbose_name=u('contacts'))
    logo = models.ImageField(null=False, blank=False, verbose_name=u('logo'))
    background = models.ImageField(null=False, blank=False, verbose_name=u('background'))

class Block(models.Model):
    landing_page = models.ForeignKey(LandingPage)
    header = models.CharField(max_length=512, null=False, blank=False, verbose_name=u('header'))
    content = models.CharField(max_length=1024, null=False, blank=False, verbose_name=u('content'))
    block_image = models.ImageField(blank=False, null=False, verbose_name=u('block_image'))


class EmailSettings(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, verbose_name=u('user'))
    to = models.EmailField(max_length=1024, verbose_name=u('to'))



