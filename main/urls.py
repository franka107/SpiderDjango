from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf import settings



router = routers.DefaultRouter()
router.register(r'currentmovements', views.CurrentMovementViewSet)
router.register(r'pastmovements', views.PastMovementViewSet)
router.register(r'robots', views.RobotViewSet)
router.register(r'sensors', views.SensorViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'reads', views.ReadViewSet)


urlpatterns = [
    path('' , include(router.urls)),
    path('register/' , views.RegisterView.as_view())
]

