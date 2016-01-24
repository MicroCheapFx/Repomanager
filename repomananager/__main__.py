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
        sample_repo.deploy(args.sample)

    elif args.django :
        create_repo(args.django[0], remote, remoteGitDir, packages=['django'])
        django_repo.deploy(args.django[0], args.django[1])

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
    command = "git init --bare " + remoteGitDir + project
    subprocess.run(["ssh", remote, command])
    command = "clone"
    target = "ssh://"+ remote + remoteGitDir + project
    subprocess.run(["git", command, target])
    pew.pew.mkvirtualenv(project, python=python, packages=packages)


def delete_repo(project, localRepoDir, remote="yuno", remoteGitDir="/var/git/"):
    command = "rm -rvf " + remoteGitDir + project
    subprocess.run(["ssh", remote, command])
    subprocess.run(["rm", "-rvf", localRepoDir + project])
    pew.pew.rmvirtualenvs([project])


if __name__ == '__main__':
    main()
