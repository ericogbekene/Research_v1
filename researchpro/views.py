from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Department, Project, Writer, HireWriter, JobStatus
from .serializers import (
    DepartmentSerializer, 
    ProjectSerializer, 
    WriterSerializer, 
    HireWriterSerializer, 
    JobStatusSerializer
)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class JobStatusViewSet(viewsets.ModelViewSet):
    queryset = JobStatus.objects.all()
    serializer_class = JobStatusSerializer

class HireWriterViewSet(viewsets.ModelViewSet):
    queryset = HireWriter.objects.all()
    serializer_class = HireWriterSerializer
    
    @action(detail=True, methods=['get'])
    def get_job_status(self, request, pk=None):
        hire_writer = self.get_object()
        job_status = hire_writer.job_status
        status = job_status.status if job_status else "Pending"
        return JsonResponse({'status': status})
