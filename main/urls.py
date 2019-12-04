from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'currentmovements', views.CurrentMovementViewSet)

router.register(r'pastmovements', views.PastMovementViewSet)
router.register(r'robots', views.RobotViewSet)
router.register(r'sensors', views.SensorViewSet)



urlpatterns = [

    path('', include(router.urls)),
    path('hola/', views.HelloView.as_view()),
    path('temperaturas/', views.RecordsViewSet.as_view())
]

#urlpatterns = router.urls

