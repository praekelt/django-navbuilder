from django import template
from django.contrib.contenttypes.models import ContentType

from navbuilder.models import Menu, MenuItem

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


@register.inclusion_tag(
    "navbuilder/inclusion_tags/breadcrumbs.html", takes_context=True
)
def navbuilder_breadcrumbs(context, slug):
    """
    Render the breadcrumbs, based on the current object. Prefer using the
    structure of the menu designated by slug, but use any menu available.
    Typical use case for this would be if the main menu has an about/terms
    page, but it's mirrored in the footer menu in a much flatter layout. We
    prefer the main menu structure. This also allows us to construct
    breadcrumbs for items that don't show up in page menus at all.
    """
    context["navbuilder_breadcrumbs"] = []
    if "object" not in context:
        return context

    def get_menuitems(item):
        if item.parent:
            struct = get_menuitems(item.parent)
            struct.append(item)
            return struct
        return [item]

    content_type = ContentType.objects.get_for_model(context["object"])
    crumb_sets = []
    for item in MenuItem.objects.filter(
            link_content_type__pk=content_type.id,
            link_object_id = context["object"].id):

        crumb_sets.append(get_menuitems(item))

    for crumb_set in crumb_sets:
        menu = crumb_set[0].menu
        if menu and menu.slug == slug:
            context["navbuilder_breadcrumbs"] = crumb_set

    if not context["navbuilder_breadcrumbs"]:
        if crumb_sets:
            context["navbuilder_breadcrumbs"] = crumb_sets[0]
        else:
            context["navbuilder_breadcrumbs"] = []

    return context
