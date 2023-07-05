from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('post/<int:id_post>/',views.post,name='post'),
    path('delete/<int:Todo_id>/',views.delete,name='delete'),
] 