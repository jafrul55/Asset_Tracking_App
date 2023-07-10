from django.urls import include,path
from rest_framework import routers
from .views import AssetViewSet,CompanyViewSet,EmployeeViewSet,DeviceViewSet,DeviceLogViewSet

router = routers.DefaultRouter()
router.register('companies',CompanyViewSet),
router.register('employees',EmployeeViewSet),
router.register('devices',DeviceViewSet),
router.register('assets',AssetViewSet),
router.register('devicelog',DeviceLogViewSet),


urlpatterns = [
    path('',include(router.urls)),
]

