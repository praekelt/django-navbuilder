from django.conf import settings


SETTINGS = getattr(settings, "NAVBUILDER", {"LINK_MODEL": "link.models.Link"})
