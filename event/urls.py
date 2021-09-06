from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('event', views.EventViewSet)

app_name = 'event'

urlpatterns = [
    path('', include(router.urls)),
]
