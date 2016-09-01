from django.contrib import admin

from navbuilder.forms import MenuAdminForm, MenuItemAdminForm
from navbuilder.models import Menu, MenuItem


class MenuItemInline(admin.StackedInline):
    form = MenuItemAdminForm
    model = MenuItem


class MenuAdmin(admin.ModelAdmin):
    form = MenuAdminForm
    list_display = ["title"]
    inlines = [MenuItemInline]


admin.site.register(Menu, MenuAdmin)
