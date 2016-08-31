from django import forms


from navbuilder.models import Menu, MenuItem


class MenuAdminForm(forms.ModelForm):
    class Meta:
        model = Menu


class MenuItemAdminForm(forms.ModelForm):
    class Meta:
        model = MenuItem
