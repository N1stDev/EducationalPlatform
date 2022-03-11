from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('forum', views.forum, name="forum"),
    path('personal-area', views.persar, name="persar"),
    path('archive', views.archive, name="archive"),
    path('consultations', views.consult, name="consult"),
]