from __future__ import unicode_literals
from fabric.operations import local, run
from fabric.api import env, task

from . import settings
from . import install
from . import photo_scraper

from fabric.contrib import django


# env.user = 'bruce'
# env.code = '/home/%s/Machines/fullstackcoder' % env.user
# env.branch = 'master'

@task
def localhost():
	env.user = settings.USER
	env.code = settings.CLIENT_PATH
	env.run = local
	env.hosts = ['localhost']