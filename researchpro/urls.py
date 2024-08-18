from rest_framework import routers
from django.urls import path, include
from .views import (DepartmentViewSet, 
                    ProjectViewSet, 
                    WriterViewSet, 
                    JobStatusViewSet, 
                    HireWriterViewSet)

router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'writers', WriterViewSet)
router.register(r'job_statuses', JobStatusViewSet)
router.register(r'hire_writers', HireWriterViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
