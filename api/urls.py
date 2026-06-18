from django.urls import path, include
from alerts import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('categories', views.AlertCategoryViewSet)
router.register('alerts', views.AlertViewSet)

alert_router = routers.NestedDefaultRouter(router, 'alerts', lookup='alert')
alert_router.register('images', views.AlertImageViewSet, basename='alert-images')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(alert_router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]