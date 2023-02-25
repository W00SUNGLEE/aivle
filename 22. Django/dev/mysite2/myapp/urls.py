from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.hello),
    path('contact/<int:id>/', views.contact)
]
