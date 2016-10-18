from django.test import TestCase

from navbuilder.tests.test_base import load_fixtures


class ModelTestCase(TestCase):
    def setUp(self):
        load_fixtures(self)

    def test_link(self):
        for key, value in self.link_data.items():
            self.assertEqual(getattr(self.link, key), value)

    def test_menu(self):
        for key, value in self.menu_data.items():
            self.assertEqual(getattr(self.menu, key), value)
        self.assertEqual(unicode(self.menu), self.menu.title)

    def test_menuitem(self):
        for key, value in self.menuitem_data.items():
            self.assertEqual(getattr(self.menuitem, key), value)
        for key, value in self.sub_menuitem_data.items():
            self.assertEqual(getattr(self.sub_menuitem, key), value)
        self.assertEqual(self.sub_menuitem.parent, self.menuitem)
        self.assertEqual(unicode(self.menuitem), self.menuitem.title)
