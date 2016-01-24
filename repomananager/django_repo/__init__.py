#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pew


def deploy(project, app, author='joe', password="qaqaqaqa" ):
    """django.deploy() deocsting

    Deploys a Django project
    :project: name of the django project to deploy
    :app: main app to deploy inside project
    :returns: TODO

    """
    print("Django project deployement.")
    print("===========================")

    os.chdir(project)
    pew.pew.inve(project, 'django-admin', 'startproject', project)

    os.chdir(project)
    pew.pew.inve(project, 'django-admin', 'startapp', app)
    pew.pew.inve(project, 'python', './manage.py', 'migrate' )
    pew.pew.inve(project, 'python', './manage.py', 'createsuperuser', '--username='+author, '--password='+password)

    pass
