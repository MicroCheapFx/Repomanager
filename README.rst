RepoManager
===========

This module aim to make deployement of various python apps easier

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

.. code:: python

It would deploy :

- Sample python project
- Django project
- Mezzanine project
- Flask project

TODO
----
- Bunch of stuff
