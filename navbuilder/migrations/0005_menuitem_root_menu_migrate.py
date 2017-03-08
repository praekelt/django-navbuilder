# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-07 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def do_save_work(context):
    """Adapted from the real save method because the real model is not
    available during a migration."""

    parent = context.parent
    while getattr(parent, "parent", None) is not None:
        if parent is context:
            break
        parent = parent.parent
    if parent is not None:
        context.root_menu = parent.menu
    else:
        context.root_menu = context.menu

    context.save()

    # Set root menu for descendants. This will trigger the required
    # recursion.
    for child in context.submenuitems.all():
        do_save_work(child)


def set_root_menu(apps, schema_editor):
    MenuItem = apps.get_model("navbuilder", "MenuItem")
    for obj in MenuItem.objects.filter(parent=None):
        obj.save()
        do_save_work(obj)


class Migration(migrations.Migration):

    dependencies = [
        ('navbuilder', '0004_menuitem_root_menu'),
    ]

    operations = [
        migrations.RunPython(set_root_menu),
    ]
