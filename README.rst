python-luftdaten
================

Python client for interacting with `sensor.community <https://sensor.community/>`_ (previously known as `luftdaten.info <http://luftdaten.info/>`_.

This module is not official, developed, supported or endorsed by sensor.community/luftdaten.info.

Installation
------------

The module is available from the `Python Package Index <https://pypi.python.org/pypi>`_.

.. code:: bash

    $ pip3 install luftdaten

On a Fedora-based system or on a CentOS/RHEL machine with has EPEL enabled.

.. code:: bash

    $ sudo dnf -y install python3-luftdaten

For Nix or NixOS is `pre-packed module <https://search.nixos.org/packages?channel=unstable&from=0&size=50&sort=relevance&query=luftdaten>`_
available. The lastest release is usually present in the ``unstable`` channel.

.. code:: bash

    $ nix-env -iA nixos.python39Packages.luftdaten

Usage
-----

The file ``example.py`` contains an example about how to use this module.

License
-------

``python-luftdaten`` is licensed under MIT, for more details check LICENSE.
