from django.conf.urls import url

from navbuilder.views import MenuDetailView, MenuListView


app_name = "navbuilder"
urlpatterns = [
    url(r'^$', MenuListView.as_view(), name="menu-list"),
    url(r'^(?P<slug>[-\w]+)/$', MenuDetailView.as_view(), name="menu-detail")
]
