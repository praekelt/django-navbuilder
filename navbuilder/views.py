from django.views import generic

from navbuilder.models import Menu


class MenuDetailView(generic.detail.DetailView):
    model = Menu
    template = "navbuilder/menu_detail.html"


class MenuListView(generic.list.ListView):
    model = Menu
    template = "navbuilder/menu_list.html"
