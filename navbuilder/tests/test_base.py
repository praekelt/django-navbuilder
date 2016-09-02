from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import Client

from navbuilder import models


class ModelTestCase(TestCase):
    def setUp(self):
        self.menu_data = {
            "title": "Menu 1",
            "slug": "menu-1"
        }
        self.menu = models.Menu.objects.create(**self.menu_data)

        self.link_data = {
            "title": "Menu 1",
            "slug": "menu-1",
            "url": "/link/1/"
        }
        self.link = models.LINK_MODEL.objects.create(**self.link_data)

        self.menuitem_data = {
            "title": "Menu Item 1",
            "slug": "menu-item-1",
            "position": 1,
            "menu": self.menu,
            "link": self.link
        }
        self.menuitem = models.MenuItem.objects.create(**self.menuitem_data)

        self.sub_menuitem_data = {
            "title": "Menu Item 1",
            "slug": "menu-item-1",
            "position": 1,
            "menu": self.menu,
            "parent": self.menuitem,
            "link": self.link
        }
        self.sub_menuitem = models.MenuItem.objects.create(
            **self.sub_menuitem_data
        )

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

    def test_detail(self):
        pass

    def test_list(self):
        pass

    def tearDown(self):
        pass
