from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view),
    path('about', views.about_view, name='about'),
    path('team', views.team_view, name='team'),
    path('news', views.news_view, name='news'),
    path('appointment', views.appointment_view, name='appointment'),
]

