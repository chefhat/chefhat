from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<str:id>', views.show, name="show"),
]
