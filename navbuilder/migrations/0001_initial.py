# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-01 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('link', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text=b'A short descriptive title.', max_length=256)),
                ('slug', models.SlugField(max_length=256)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text=b'A short descriptive title.', max_length=256)),
                ('slug', models.SlugField(max_length=256)),
                ('position', models.PositiveIntegerField()),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='link.Link')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menuitems', to='navbuilder.Menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submenuitems', to='navbuilder.MenuItem')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
