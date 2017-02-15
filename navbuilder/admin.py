from django.contrib import admin

from navbuilder.forms import MenuAdminForm, MenuItemAdminForm
from navbuilder.models import Menu, MenuItem


class MenuItemInline(admin.StackedInline):
    form = MenuItemAdminForm
    model = MenuItem
    prepopulated_fields = {"slug": ["title"]}


class MenuAdmin(admin.ModelAdmin):
    form = MenuAdminForm
    list_display = ["title"]
    inlines = [MenuItemInline]
    prepopulated_fields = {"slug": ["title"]}
    search_fields = ["title", "slug"]


class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemAdminForm
    list_display = ["title", "parent", "_get_absolute_url"]
    prepopulated_fields = {"slug": ["title"]}
    search_fields = ["title", "slug"]
    list_filter = ["menu"]

    def _get_absolute_url(self, obj):
        try:
            url = obj.link.get_absolute_url()
        except AttributeError:
            url = None
        if url:
            return "<a href=\"%s\" target=\"public\">%s</a>" % (url, url)
        return "<p class=\"errornote\">Inactive or broken link</p>"

    _get_absolute_url.short_description = "Permalink"
    _get_absolute_url.allow_tags = True


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
