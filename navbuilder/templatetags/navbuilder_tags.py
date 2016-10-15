from django import template

from navbuilder.models import Menu

register = template.Library()


@register.inclusion_tag(
    "navbuilder/inclusion_tags/menu_detail.html", takes_context=True
)
def render_menu(context, slug):
    try:
        context["object"] = Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        pass
    return context


@register.inclusion_tag(
    "navbuilder/inclusion_tags/menuitem_detail.html", takes_context=True
)
def render_menuitem(context, obj):
    context["object"] = obj
    return context
