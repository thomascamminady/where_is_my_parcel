===================
Where is my parcel?
===================


.. image:: https://img.shields.io/pypi/v/where_is_my_parcel.svg
        :target: https://pypi.python.org/pypi/where_is_my_parcel

.. image:: https://img.shields.io/travis/thomascamminady/where_is_my_parcel.svg
        :target: https://travis-ci.com/thomascamminady/where_is_my_parcel

.. image:: https://readthedocs.org/projects/where-is-my-parcel/badge/?version=latest
        :target: https://where-is-my-parcel.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A better tracking app.


Setup
--------
Place a file called ``.credentials.json`` inside ``where_is_my_parcel/where_is_my_parcel/backend/`` that has your DHL and Mapbox keys, looking like this::

    {
      "dhl": {
        "api_key": "123456.....",
        "api_secret": "abcdef...."
      },
      "mapbox": {
        "api_key": "XYZ..."
      }    
    }






Credits
-------

This package was created with Cookiecutter_ and `thomascamminady/cookiecutter-pypackage`_, a fork of the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`thomascamminady/cookiecutter-pypackage`: https://github.com/thomascamminady/cookiecutter-pypackage
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
