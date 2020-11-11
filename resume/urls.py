from django.urls import path
from . import views
from .views import *



app_name = 'resume'

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about', views.AboutView, name='about'),
    path('portfolio', views.PortfolioView, name='portfolio'),
    path('contact', views.ContactView, name='contact'),
    #path('dashboard/portfolio/edit/<str:pk>', PortfolioEdit.as_view(), name="portfolio-edit")

]