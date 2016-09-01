from django import forms


from navbuilder.models import Menu, MenuItem


class MenuAdminForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["title", "slug"]


class MenuItemAdminForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["title", "slug", "position", "menu", "parent", "link"]

    def clean_parent(self):
        pass
