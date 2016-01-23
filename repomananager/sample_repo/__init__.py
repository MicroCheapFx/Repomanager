#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os

def deploy(project):
    """django.deploy() deocsting

    Deploys a sample python project
    :project: name of the django project to deploy
    :returns: TODO

    """
    print("Sample project deployement.")
    print("===========================")

    subprocess.run(["pwd"])
    os.chdir(project)
    subprocess.run(["pwd"])
    subprocess.run(["mkdir", project])
    subprocess.run(["touch", project +"/__init__.py"])
    
    
    pass
