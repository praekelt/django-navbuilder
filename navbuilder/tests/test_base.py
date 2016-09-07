from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

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
        "link": kls.link
    }
    kls.sub_menuitem = models.MenuItem.objects.create(
        **kls.sub_menuitem_data
    )


class ModelTestCase(TestCase):
    def setUp(self):
        load_fixtures(self)

    def test_link(self):

        # ensure the data was saved correctly
        for key, value in self.link_data.items():
            self.assertEqual(getattr(self.link, key), value)

    def test_menu(self):

        # ensure the data was saved correctly
        for key, value in self.menu_data.items():
            self.assertEqual(getattr(self.menu, key), value)

    def test_menuitem(self):

        # ensure the data was saved correctly
        for key, value in self.menuitem_data.items():
            self.assertEqual(getattr(self.menuitem, key), value)

        # ensure the sub menu item data was saved correctly
        for key, value in self.sub_menuitem_data.items():
            self.assertEqual(getattr(self.sub_menuitem, key), value)

        # ensure the parent menu item is accessible
        self.assertEqual(self.sub_menuitem.parent, self.menuitem)


class AdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.editor = get_user_model().objects.create(
            username="editor",
            email="editor@test.com",
            is_superuser=True,
            is_staff=True
        )
        self.editor.set_password("password")
        self.editor.save()
        self.client.login(username="editor", password="password")

    def test_admin(self):
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)

    def test_admin_menu(self):
        response = self.client.get("/admin/navbuilder/menu/add/")
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        load_fixtures(self)

    def test_detail(self):
        response = self.client.get(
            reverse(
                "navbuilder:menu-detail",
                kwargs={"slug": self.menu_data["slug"]}
            )
        )

        # ensure the menu contains all elements
        self.assertContains(response, self.menu.slug)
        self.assertContains(response, self.menuitem.slug)
        self.assertContains(response, self.sub_menuitem.slug)
        self.assertContains(response, self.menuitem.link.slug)

    def test_list(self):
        menu_data2 = {
            "title": "Menu 2 Title",
            "slug": "menu-2-title"
        }
        menu2 = models.Menu.objects.create(**menu_data2)
        response = self.client.get(reverse("navbuilder:menu-list"))

        # ensure the menu lst is rendered correctly
        self.assertContains(response, self.menu.slug)
        self.assertContains(response, menu2.slug)

    def tearDown(self):
        pass
