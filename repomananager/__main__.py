#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import subprocess
import os

from prompt import color_print, question
import sample_repo
import django_repo
import mezzanine_repo
import flask_repo

localRepoDir = os.environ["HOME"]+"/srv/"



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
    #parser.add_argument('name', metavar='name', type=str)
    #parser.add_argument('-y', '--yes', action='store_true', help='answer to all question default answer')
    args = parser.parse_args()
    os.chdir(localRepoDir)
    savedPath = os.getcwd()

    if args.sample :
        create_repo(args.sample)
        sample_repo.deploy(args.sample)

    if args.django :
        create_repo(args.django[0])
        sample_repo.deploy(args.django[0], args.django[1])
        print("Not Implemented Yet.")

    if args.mezzanine :
        create_repo(args.mezzanine)
        sample_repo.deploy(args.mezzanine)
        print("Not Implemented Yet.")

    if args.flask :
        create_repo(args.flask)
        sample_repo.deploy(args.flask)
        print("Not Implemented Yet.")
    
    os.chdir(savedPath)

    if args.delete :
        delete_repo(args.delete)
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


def create_repo(name,remote="yuno",remoteGitDir="/var/git/"):
    command = "git init --bare " + remoteGitDir + name
    subprocess.run(["ssh", remote, command])
    command = "clone"
    target = "ssh://"+ remote + remoteGitDir + name
    subprocess.run(["git", command, target])


def delete_repo(name,remote="yuno",remoteGitDir="/var/git/"):
    command = "rm -rvf " + remoteGitDir + name
    subprocess.run(["ssh", remote, command])


if __name__ == '__main__':
    main()
