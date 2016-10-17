from link.models import Link

from navbuilder import models


def load_fixtures(kls):
    kls.menu_data = {
        "title": "Menu 1",
        "slug": "menu-1"
    }
    kls.menu = models.Menu.objects.create(**kls.menu_data)

    kls.link_data = {
        "title": "Link 1",
        "slug": "link-1",
        "url": "/link/1/"
    }
    kls.link = Link.objects.create(**kls.link_data)

    kls.menuitem_data = {
        "title": "Menu Item 1",
        "slug": "menu-item-1",
        "position": 1,
        "menu": kls.menu,
        "link": kls.link
    }
    kls.menuitem = models.MenuItem.objects.create(**kls.menuitem_data)

    kls.sub_menuitem_data = {
        "title": "Sub Menu Item 1",
        "slug": "sub-menu-item-1",
        "position": 1,
        "parent": kls.menuitem,
        "target": "blank",
        "link": kls.link
    }
    kls.sub_menuitem = models.MenuItem.objects.create(
        **kls.sub_menuitem_data
    )
