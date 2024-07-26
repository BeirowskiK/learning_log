from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Include default Django auth paths
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]