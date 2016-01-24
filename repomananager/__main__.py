#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import subprocess
import os
import configparser
import pew


from prompt import color_print, question
import sample_repo
import django_repo
import mezzanine_repo
import flask_repo



def main():
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
        pew.pew.mkvirtualenv(args.sample)
        #subprocess.run(["pew", "new", venvDir])
        sample_repo.deploy(args.sample)

    elif args.django :
        print("DEBUG 00")
        create_repo(args.django[0], remote, remoteGitDir)
        print("DEBUG 01")
        pew.pew.mkvirtualenv(args.django[0], packages=['django'])
        #venvDir = os.environ["WORKON_HOME"]+"/"+args.django[0]
        #print(venvDir)
        #subprocess.run(["virtualenv", venvDir])
        print("DEBUG 02")
        django_repo.deploy(args.django[0], args.django[1])
        print("DEBUG 03")

    elif args.mezzanine :
        create_repo(args.mezzanine)
        pew.pew.mkvirtualenv(args.mezzanine, python='python3.3', packages=['mezzanine'])
        mezzanine_repo.deploy(args.mezzanine)
        print("Not Implemented Yet.")

    elif args.flask :
        create_repo(args.flask)
        pew.pew.mkvirtualenv(args.flask, packages=['flask'])
        flask_repo.deploy(args.flask)
        print("Not Implemented Yet.")
    
    os.chdir(savedPath)


    if args.delete :
        delete_repo(args.delete, localRepoDir)
        #pew.pew.rmvirtualenvs([name])
        #venvDir = os.environ["WORKON_HOME"]+"/"+args.delete
        #subprocess.run(["pew", "wipeenv", args.delete])
        #subprocess.run(["rm", "-rvf", venvDir])
        subprocess.run(["rm", "-rvf", localRepoDir + args.delete])


#    if args.create :
        #savedPath = os.getcwd()
        #print(localRepoDir)
        ##subprocess.run(["virtualenv", os.environ["WORKON_HOME"]+"/"+args.name])
        #if args.django :
            #os.chdir(localRepoDir)
            #django_deploy.deploy(args.name, args.app)
            #pass
        #else :
            #os.chdir(localRepoDir)
            #print("Initalizing sample python module repository")
            #happiness = question("Are you Happy?", "Yes I am.")
            #print(happiness)
            #pass
        #os.chdir(savedPath)

    #if args.delete :
        #delete_repo(args.name)


def create_repo(name, remote, remoteGitDir):
    command = "git init --bare " + remoteGitDir + name
    subprocess.run(["ssh", remote, command])
    command = "clone"
    target = "ssh://"+ remote + remoteGitDir + name
    subprocess.run(["git", command, target])


def delete_repo(name, localRepoDir, remote="yuno", remoteGitDir="/var/git/"):
    command = "rm -rvf " + remoteGitDir + name
    subprocess.run(["ssh", remote, command])
    command = "rm -rvf " + localRepoDir + name
    pew.pew.rmvirtualenvs([name])


if __name__ == '__main__':
    main()
