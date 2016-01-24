#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
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

    subprocess.run(["pwd"])
    #os.chdir(project)
    #subprocess.run(["pwd"])
    #subprocess.run(["mkdir", project])
    #subprocess.run(["touch", project +"/__init__.py"])
    #source = os.path.abspath(repomanager.__file__)
    #source = os.path.abspath(sample_repo.__file__)
    #print(source)
    destination = 'uuuu'
    print(destination)
    tempDir = "/tmp/"+project
    shutil.rmtree(tempDir)  
    shutil.copytree(project, tempDir)
    shutil.rmtree(project)
    shutil.copytree(source, project)
    shutil.copytree(tempDir+"/.git", project+"/.git")
    
    shutil.copytree(project+"/sample", project+"/"+project)
    shutil.rmtree(project+"/sample")
    
    pass
