============================
bobtemplates.redturtle.plone
============================

``bobtemplates.redturtle.plone`` provides `mr.bob <http://mrbob.readthedocs.org/en/latest/>`_ template to generate buildout for RedTurtle projects.

.. note::

   Use `plonecli <https://pypi.python.org/pypi/plonecli>`_ with this plugin for better integration.

Features
========

Buildout created with ``bobtemplates.redturtle.plone`` comes with battery included.

They already have a preset configurations for:

- Process manager
- Plone
- Varnish

Provided templates
==================

- buildout_redturtle


Installation
============

You can install bobtemplates.redturtle.plone as every other normal Python package with `pip <https://pypi.python.org/pypi/pip>`_ inside a `virtualenv <https://pypi.python.org/pypi/virtualenv>`_.


Installation with pip in a virtualenv
-------------------------------------

You can install ``bobtemplates.redturtle.plone`` with pip in a virtualenv.
If you don't have an active virtualenv, you can create one inside your project directory.

.. code-block:: bash

    virtualenv .

Then either activate the virtualenv:

.. code-block:: bash

    source ./bin/activate

or just use the binaries directly inside the bin folder as below:

.. code-block:: console

    ./bin/pip install bobtemplates.redturtle.plone


Use in a buildout
-----------------

.. code-block:: ini

    [buildout]
    parts += mrbob

    [mrbob]
    recipe = zc.recipe.egg
    eggs =
        bobtemplates.redturtle.plone

This creates a mrbob-executable in your bin-directory.

Usage
-----

As bobtemplates.redturtle.plone is a template for mr.bob_, we use mrbob to run the templates.

If you are using `buildout <https://pypi.python.org/pypi/zc.buildout>`_  or an unactivated `virtualenv <https://pypi.python.org/pypi/virtualenv>`_, you can use mrbob like this:

.. code-block:: console

    ./bin/mrbob bobtemplates.redturtle.plone:buildout_redturtle -O /some/path/myproject.buildout

If you are using an activated virtualenv, you can use mrbob like this:


Activate your virtualenv:

.. code-block:: console

    source bin/activate

.. code-block:: console

    mrbob bobtemplates.redturtle.plone:buildout_redturtle -O /some/path/myproject.buildout

This will create your Plone buildout inside the ``/some/path`` directory.

See the documentation of mr.bob_ for further information.

Contribute
==========

- Issue Tracker: https://github.com/RedTurtle/bobtemplates.redturtle.plone/issues
- Source Code: https://github.com/RedTurtle/bobtemplates.redturtle.plone
