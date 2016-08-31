from importlib import import_module

from django.db import models

from navbuilder import SETTINGS


LINK_MODEL = import_module(SETTINGS["LINK_MODEL"])


class Menu(models.Model):
    title = models.CharField(
        max_length=256, help_text="A short descriptive title."
    )
    slug = models.SlugField(
        max_length=256, db_index=True
    )

    class Meta:
        ordering = ["title"]

    def __unicode__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(
        max_length=256, help_text="A short descriptive title."
    )
    slug = models.SlugField(
        max_length=256, db_index=True
    )
    position = models.PositiveIntegerField()
    menu = models.ForeignKey(Menu, related_name="menuitems")
    parent = models.ForeignKey(
        "self", related_name="submenuitems", blank=True, null=True
    )
    link = models.ForeignKey(LINK_MODEL)

    class Meta:
        ordering = ["title"]

    def __unicode__(self):
        return self.title
