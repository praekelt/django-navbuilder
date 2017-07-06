Django Navbuilder
=================
**Build hierarchical navigation objects from multiple link objects**

.. image:: https://travis-ci.org/praekelt/django-navbuilder.svg?branch=develop
    :target: https://travis-ci.org/praekelt/django-navbuilder

.. image:: https://coveralls.io/repos/github/praekelt/django-navbuilder/badge.svg?branch=develop
    :target: https://coveralls.io/github/praekelt/django-navbuilder?branch=develop

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``django-navbuilder`` to your Python path.

#. Add ``navbuilder`` to your ``INSTALLED_APPS`` setting.

#. Add ``url(r'^navbuilder/', include("navbuilder.urls", namespace="navbuilder"))`` to your ``url patterns`` (only required if you intend on using the list/detail views)

Usage
-----

Include the navbuilder templatetags:

``{% load navbuilder_tags %}``

Use the inclusion tag which has been provided:
``{% render_menu slug %}``

Breadcrumbs
-----------

The breadcrumbs tag tries to render breadcrumbs, based on the current object.
It does this by trying to find a menu item that points to context["object"],
and then constructs a breadcrumb trail depending on the menu structure.  It
prefers using the structure of the menu designated by slug, but will use any
menu available. Typical use case for this would be if the main menu has an
about/terms page, but it's mirrored in the footer menu in a much flatter
layout. We prefer the main menu structure. This also allows us to construct
breadcrumbs for items that don't show up in page menus at all.

Inclusion tag usage:
``{% navbuilder_breadcrumbs slug %}``

The very specific naming for the tag is used so that it could be used with
other breadcrumb generators as a fallback.

