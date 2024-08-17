from rest_framework import serializers
from .models import Department, Project, Writer, HireWriter, JobStatus


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description']

    def __str__(self):
        """
        Return a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.name
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'number_of_pages', 'doctype', 'keywords', 'project_level', 'project_type', 'created_at', 'updated_at', 'abstract', 'department', 'author']

    def __str__(self):
        """
        Return a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.title
class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ['id', 'name', 'email', 'department', 'status', 'created_at', 'exprerience', 'rating']


class JobStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobStatus
        fields = ['id', 'researcher', 'status']


    def __str__(self):
        """
        Return a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.name
    

class HireWriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireWriter
        fields = ['id', 'project_topic', 'name', 'email', 'phone', 'writer', 'created_at',]

    def __str__(self):
        """
        Return a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.name
