from django import template

register = template.Library()


@register.inclusion_tag(
    "navbuilder/inclusion_tags/menu_detail.html", takes_context=True
)
def render_menu(context, obj):
    context["object"] = obj
    return context


@register.inclusion_tag(
    "navbuilder/inclusion_tags/menuitem_detail.html", takes_context=True
)
def render_menuitem(context, obj):
    context["object"] = obj
    return context
