# Generated by Django 5.0.4 on 2024-08-14 21:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchpro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hirewriter',
            name='status',
        ),
        migrations.CreateModel(
            name='JobStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('ongoing', 'Ongoing'), ('cancelled', 'Cancelled'), ('pending', 'Pending')], max_length=16)),
                ('researcher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researchpro.writer')),
            ],
        ),
    ]
