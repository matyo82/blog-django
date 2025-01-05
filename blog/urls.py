from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/<slug:slug>/', views.ArticleDetailView.as_view(), name='blog_detail'),
]
