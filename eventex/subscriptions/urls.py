
from django.urls import path
from eventex.subscriptions.views import subscribe, detail

urlpatterns = [
    path('', subscribe, name='new'),
    path('<int:pk>', detail, name='detail'),
]
