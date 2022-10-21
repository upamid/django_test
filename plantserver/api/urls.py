from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UsersViewSet

v1_router = DefaultRouter()
v1_router.register('users', UsersViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(v1_router.urls)),
]
