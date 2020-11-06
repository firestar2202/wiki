from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.random, name="random"),
    path("search", views.get_search, name="search"),
    path("<str:pagename>", views.page, name="page")
]
