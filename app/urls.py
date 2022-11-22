from django.urls import path, include
from .views import index, details, dashboard


urlpatterns = [
    path('', index, name='index'),
    path('auth/', include('django.contrib.auth.urls') ),
    path('details/', details, name='details'),
    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),
]