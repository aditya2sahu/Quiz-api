
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from. import views
#
# router=DefaultRouter
# router.register("all",views.delquiz.as_view(),basename="allname")

urlpatterns = [
    path("",views.Home.as_view(),name="Home"),
    path("login", views.LoginView.as_view(), name="login"),
    path("register", views.register.as_view(), name="register"),
    path("Change", views.changepassword.as_view(), name="register"),
]
