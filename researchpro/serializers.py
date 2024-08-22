from rest_framework import serializers
from .models import Department, Project, Writer, HireWriter, JobStatus


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description']


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'number_of_pages', 'doctype', 'keywords', 'project_level', 'project_type', 'created_at', 'updated_at', 'abstract', 'department', 'author']


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ['id', 'name', 'email', 'department', 'status', 'created_at', 'experience', 'rating']


class JobStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobStatus
        fields = ['id', 'researcher', 'status']


class HireWriterSerializer(serializers.ModelSerializer):
    writer = serializers.StringRelatedField()

    class Meta:
        model = HireWriter
        fields = ['id', 'project_topic', 'name', 'email', 'phone', 'writer', 'created_at']
