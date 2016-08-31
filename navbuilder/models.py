from importlib import import_module

from django.db import models

from navbuilder import SETTINGS


LINK_PATH = SETTINGS["LINK_MODEL"].split(".")
LINK_MODULE = import_module(".".join(LINK_PATH[:-1]))
LINK_MODEL = getattr(LINK_MODULE, LINK_PATH[-1])


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
