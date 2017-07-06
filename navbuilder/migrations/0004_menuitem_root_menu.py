# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-07 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navbuilder', '0003_auto_20161017_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='root_menu',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='navbuilder.Menu'),
        )
    ]
