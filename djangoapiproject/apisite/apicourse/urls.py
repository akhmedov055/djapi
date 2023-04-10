from django.contrib import admin
from django.urls import path, include

from apicourse.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', CourseHome.as_view()),
]