from django.urls import path
from .views import*

urlpatterns = [
    path('',home,name="home"),
    path('menu/',menu,name="menu"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('addmenu/',addmenu,name="addmenu"),
    path('login/',loginform,name="login"),
    path('register/',register,name="register"),
    path('logout/',logoutform,name="logout"),
    path('bookseat/',bookseat,name="bookseat"),
]
