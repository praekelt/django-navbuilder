from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import Client

from navbuilder import models


class ModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_link(self):
        pass


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
        pass

    def test_admin_link(self):
        pass

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
