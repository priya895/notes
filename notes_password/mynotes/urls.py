from django.urls import path,include
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
      path("passwords",views.fpasswords,name="passwords"),
      path("about",views.about,name="about"),
      path("contact",views.contact,name="contact"),
      path(r'^create/',views.create,name="create"),
      path(r'^pcreate/',views.pcreate,name="pcreate"),
      path("show/<int:id>",views.fshow,name="show"),
      # path("smail",views.smail,name="smail"),
      path("nlogin",views.nlogin,name="nlogin"),
      path("blogin",views.blogin,name="blogin"),
]