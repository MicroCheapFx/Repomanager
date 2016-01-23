#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import subprocess
import os

from prompt import color_print, question

#import 

localRepoDir = os.environ["HOME"]+"/srv/"



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--yes', action='store_true', help='answer to all question default answer')
    parser.add_argument('-c', '--create', action='store_true', help='Create a new repository')
    parser.add_argument('-d', '--delete', action='store_true', help='Deletei an existing repository')
    parser.add_argument('-dj', '--django', action='store_true', help='Create a new django repository')
    parser.add_argument('name', metavar='name', type=str)
    args = parser.parse_args()

    if args.create :
        savedPath = os.getcwd()
#        create_repo(args.name)
        print(localRepoDir)
        #subprocess.run(["virtualenv", os.environ["WORKON_HOME"]+"/"+args.name])
        if args.django :
            os.chdir(localRepoDir)
            print("Initalizing django repository")
            subprocess.run(["pew", "in", args.name, "pip", "install", "django"])
            subprocess.run(["pew", "in", args.name, "django-admin", "startproject", args.name])
            pass
        else :
            os.chdir(localRepoDir)
            print("Initalizing sample python module repository")
            happiness = question("Are you Happy?", "Yes I am.")
            print(happiness)
            pass
        os.chdir(savedPath)

    if args.delete :
        delete_repo(args.name)


def create_repo(name,remote="yuno",remoteGitDir="/var/git/"):
    command = "git init --bare " + remoteGitDir + name
    subprocess.run(["ssh", remote, command])


def delete_repo(name,remote="yuno",remoteGitDir="/var/git/"):
    command = "rm -rvf " + remoteGitDir + name
    subprocess.run(["ssh", remote, command])


if __name__ == '__main__':
    main()
