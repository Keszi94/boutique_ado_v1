from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test-email/', views.email_test, name='email_test'),
]
