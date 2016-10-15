from django.test import TestCase

from navbuilder.tests.test_base import load_fixtures


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
