RepoManager
===========

  This module aim to make deployement of various python apps easierprojects easier. It might deploy projects like :

- pypa/sample
- django
- mezzanine
- flask

It first creates a git repo on a distant server, then clone it in a local repository path, then populate the project.
It also build a virtualenv (pew is required) for each project


Usage
-----

::

  repomanager -sp --sample foo

Initialize a python sample project repository::

  repomanager -dj --django foo bar

Initialize a Django project repository::

  repomanager -mz --mezzanine foo

Initialize a Mezzanine project repository::

  repomanager -fk --flask foo

Initialize a Flask project repository::

  repomanager --delete foo

Delete a project repository::


Installation
------------

Not available with pip.


TODO
----

- Implement interactive mode
- Implement import/export option (json?)
- Patch files for better debootstraping
- git commit/push at end of deployement
- github repos handling
- generate repomanager.cfg files
- repomanager.cfg file documentation
- treat repos as objects
