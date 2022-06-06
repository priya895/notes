from django.urls import path
from . import apps
from . import views
urlpatterns =[
      path("",views.active,name="index"),
      path("index", views.index, name="index"),
      path("login",views.login_view,name="login"),
      path("register",views.register,name="register"),
      path("logout",views.logout_view,name="logout"),
      path("home",views.homepage,name="homepage"),
      path("notes",views.fnotes,name="notes"),
      path("about",views.about,name="about"),
      path("contact",views.contact,name="contact"),
      path(r'^create/',views.create,name="create"),
]