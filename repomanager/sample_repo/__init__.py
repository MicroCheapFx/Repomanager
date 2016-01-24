#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
#import repomanager

def deploy(project, source):
    """sample.deploy() deocsting

    Deploys a sample python project
    :project: name of the python project to deploy
    :returns: TODO

    """
    print("Sample project deployement.")
    print("===========================")

    tempDir = "/tmp/"+project
    shutil.rmtree(tempDir)  
    shutil.copytree(project, tempDir)
    shutil.rmtree(project)
    shutil.copytree(source, project)
    shutil.copytree(tempDir+"/.git", project+"/.git")
    
    shutil.copytree(project+"/sample", project+"/"+project)
    shutil.rmtree(project+"/sample")
    
    pass
