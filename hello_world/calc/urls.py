from django.urls import path
from . import views

urlpatterns = [
    path('', views.do_nothing, name="do_nothing"),
    path('about/', views.home, name="home"),
    # path('about/', views.about, name="about")
    # path('about/', views.about, name="about")
]
