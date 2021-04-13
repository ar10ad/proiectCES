from django.urls import path, include
from .views import index, QuestionAPI, latest
from rest_framework import routers


router = routers.DefaultRouter()
router.register("question", QuestionAPI)

urlpatterns = [
    path('', index, name="index"),
    path('', include(router.urls),name='api'),
    path('latest', latest, name="latest"),
]
