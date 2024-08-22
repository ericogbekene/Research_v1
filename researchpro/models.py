from django.db import models
from django.contrib.auth.models import User

DOCTYPE_CHOICES = (
    ('pdf', 'PDF'),
    ('doc', 'DOC'),
    ('docx', 'DOCX'),
)

LEVEL_CHOICES = (
    ('nce/nd', 'NCE/ND'),
    ('hnd', 'HND'),
    ('ug', 'Undergraduate'),
    ('pg', 'Postgraduate'),
)

PROJECT_TYPE_CHOICES = (
    ('research', 'Research'),
    ('publication', 'Publication'),
    ('thesis', 'Thesis'),
    ('design', 'Design'),
    ('other', 'Other'),
)

EXPERIENCE_CHOICES = (
    ('entry', 'Entry'),
    ('experienced', 'Experienced'),
    ('expert', 'Expert'),
    ('master', 'Master'),
    ('doctor', 'Doctor'),
)

RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

WRITER_STATUS_CHOICES = (
    ('available', 'Available'),
    ('unavailable', 'Unavailable'),
)

JOB_STATUS_CHOICES = (
    ('completed', 'Completed'),
    ('ongoing', 'Ongoing'),
    ('cancelled', 'Cancelled'),
    ('pending', 'Pending'),
)

class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    doctype = models.CharField(max_length=4, choices=DOCTYPE_CHOICES)
    keywords = models.CharField(max_length=200)
    project_level = models.CharField(max_length=16, choices=LEVEL_CHOICES)
    project_type = models.CharField(max_length=16, choices=PROJECT_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    abstract = models.TextField()

    def __str__(self):
        return self.title

class Writer(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=WRITER_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    experience = models.CharField(max_length=16, choices=EXPERIENCE_CHOICES)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.name.username
    
    # def total_jobs(self):
     #   return self.jobstatus_set.count()
   # total_jobs.short_description = 'Total Jobs'

class JobStatus(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    researcher = models.ForeignKey(Writer, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=JOB_STATUS_CHOICES)

    def __str__(self):
        return self.status

class HireWriter(models.Model):
    project_topic = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    job_status = models.OneToOneField(JobStatus, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name

class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.project.title} by {self.writer.name.username} - {self.rating}/5"
