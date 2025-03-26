from django.urls import path

from api import views

urlpatterns = [
    path("clients/add/", views.ClientCreateView.as_view(), name='clients_add'),
]