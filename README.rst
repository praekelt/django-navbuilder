Django Navbuilder
=================
**Build hierarchical navigation objects from multiple link objects**

.. figure:: https://travis-ci.org/praekelt/django-navbuilder.svg?branch=develop
   :align: center
   :alt: Travis

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``django-navbuilder`` to your Python path.

#. Add ``navbuilder`` to your ``INSTALLED_APPS`` setting.

#. Add ``url(r'^navbuilder/', include("navbuilder.urls", namespace="navbuilder"))`` to your ``url patterns`` (only required if you intend on using the list/detail views)

#. If you prefer to use you're own Link model add it in: ``settings.NAVBUILDER["LINK_MODEL"]`` otherwise https://github.com/praekelt/django-link will need to be installed.

Usage
-----

Use the inclusion tag which has been provided:
``{% render_menu object %}``
