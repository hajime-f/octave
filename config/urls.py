from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('api/v1/', include('dj_rest_auth.urls')),
    path('api/v1/', include('dj_rest_auth.registration.urls')),
    path('api/v1/', include('event.urls')),
]
