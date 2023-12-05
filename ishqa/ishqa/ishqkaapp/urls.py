
from django.urls import path
from ishqkaapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('request', views.request, name='request'),
    path('save', views.save, name='save'),
    path('approved/<int:id>', views.approved, name='approved'),
]
