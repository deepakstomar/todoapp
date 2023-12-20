from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('add/', views.add_content_view, name='add_content'),
    path('delete/<int:id>/', views.delete_content_view, name='delete_content'),
]