from django.urls import path
from .views import HomeView, ServiceView, ContactView, AboutView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('servises/', ServiceView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about_us'),
]