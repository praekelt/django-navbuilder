from django.contrib import admin

from navbuilder.forms import NavBuilderAdminForm
from navbuilder.models import Menu, MenuItem


class MenuItemInline(admin.StackedInline):
    model = MenuItem


class MenuAdmin(admin.ModelAdmin):
    form = NavBuilderAdminForm
    list_display = ["title"]
    inlines = [MenuItemInline]


admin.site.register(Menu, MenuAdmin)
