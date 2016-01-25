#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Repomanager
===========

Deploy a distant git reopsitory clone it locally and build a fresh new python
project.
'''

import argparse
import subprocess
import os
import configparser
import pew

from repomanager.prompt import color_print, question
import repomanager.sample_repo
import repomanager.django_repo
import repomanager.mezzanine_repo
import repomanager.flask_repo


#class repo(name='test00', author='John Doe', python='python3.5', github=False, license='GPL'):
#
#    """Docstring for repo. """
#
#    __slots__ = ()
#
#    def __init__(self):
#        """TODO: to be defined. """
#        name='test00'.__init__(self)
#        author='John Doe'.__init__(self)
#        python='python3.5'.__init__(self)
#        github=False.__init__(self)
#       license='GPL'.__init__(self)

#class project(name, author, python, license, github=False):
#
    #"""Class for repositories. """
#
    #def __init__(self):
        #"""TODO: to be defined1. """
        #name.__init__(self)
        #author.__init__(self)
        #python.__init__(self)
        #license.__init__(self)
        #github=False.__init__(self)
#
    #def create_repo(project, remote, remoteGitDir, python="python3.5", packages=[]):
        #'''
        #Generate a distant git repository, then clone it locally and build a virtualenv
        #'''
        #command = "git init --bare " + remoteGitDir + project
        #subprocess.run(["ssh", remote, command])
        #command = "clone"
        #target = "ssh://"+ remote + remoteGitDir + project
        #subprocess.run(["git", command, target])
        #pew.pew.mkvirtualenv(project, python=python, packages=packages)
#
#
    #def delete_repo(project, localRepoDir, remote="yuno", remoteGitDir="/var/git/"):
        #'''
        #Delete a distant git repository, delete local repository and virtualenv
        #'''
        #command = "rm -rvf " + remoteGitDir + project
        #subprocess.run(["ssh", remote, command])
        #subprocess.run(["rm", "-rvf", localRepoDir + project])
        #pew.pew.rmvirtualenvs([project])
#
#
    #def create_repo(self, arg1):
        #"""TODO: Docstring for create_repo.
#
        #:arg1: TODO
        #:returns: TODO
#
        #"""
        #pass     


def main():
    ''' Docstring for MAIN FUNCTION

    Yess
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--delete',
            help='Delete an existing repository'
            )
    parser.add_argument(
            '-sp', '--sample',
            help='Create a new python sample project repository'
            )
    parser.add_argument(
            '-dj', '--django',
            nargs=2,
            help='Create a new django project repository'
            )
    parser.add_argument(
            '-mz', '--mezzanine',
            help='Create a new mezzanine project repository'
            )
    parser.add_argument(
            '-fk', '--flask',
            help='Create a new flask project repository'
            )
    parser.add_argument('-c', '--config', help="alternate config file")
    args = parser.parse_args()

    if args.config :
        configFile = args.config
    else :
        configFile = os.environ["HOME"] +"/.config/repomanager/config.cfg"

    localRepoDir = os.environ["HOME"]+"/srv/"
    print(localRepoDir)
    if os.path.isfile(configFile) :
        config = configparser.ConfigParser()
        config.read(configFile)
        author = config['USER']['name']
        email = config['USER']['email']
        remote = config['PATH']['server']
        remoteGitDir = config['PATH']['serverRepoPath']
        localRepoDir = os.environ["HOME"] + config['PATH']['localRepoPath']
        print(localRepoDir)
    else :
        print("fichier perdu.")
        localRepoDir = os.environ["HOME"]+"/srv/"


    os.chdir(localRepoDir)
    savedPath = os.getcwd()


    if args.sample :
        create_repo(args.sample, remote, remoteGitDir)

        source = os.path.abspath(sample_repo.__file__)[0:-11] + "tree"
        sample_repo.deploy(args.sample, source)

    elif args.django :
        create_repo(args.django[0], remote, remoteGitDir, packages=['django'])
        django_repo.deploy(args.django[0], args.django[1], author="fx", password="fxfxfxfx", email='john@doe.com')

    elif args.mezzanine :
        create_repo(args.mezzanine, remote, remoteGitDir, python='python3.3', packages=['mezzanine'])
        mezzanine_repo.deploy(args.mezzanine)

    elif args.flask :
        create_repo(args.flask, remote, remoteGitDir, packages=['flask'])
        flask_repo.deploy(args.flask)
    
    os.chdir(savedPath)


    if args.delete :
        delete_repo(args.delete, localRepoDir, remote, remoteGitDir)


def create_repo(project, remote, remoteGitDir, python="python3.5", packages=[]):
    '''
    Generate a distant git repository, then clone it locally and build a virtualenv
    '''
    command = "git init --bare " + remoteGitDir + project
    subprocess.run(["ssh", remote, command])
    command = "clone"
    target = "ssh://"+ remote + remoteGitDir + project
    subprocess.run(["git", command, target])
    pew.pew.mkvirtualenv(project, python=python, packages=packages)


def delete_repo(project, localRepoDir, remote="yuno", remoteGitDir="/var/git/"):
    '''
    Delete a distant git repository, delete local repository and virtualenv
    '''
    command = "rm -rvf " + remoteGitDir + project
    subprocess.run(["ssh", remote, command])
    subprocess.run(["rm", "-rvf", localRepoDir + project])
    pew.pew.rmvirtualenvs([project])


