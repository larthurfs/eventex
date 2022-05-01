from django.urls import path
from eventex.core.views import home

urlpatterns = [
    path('', home, 'home'),
]
