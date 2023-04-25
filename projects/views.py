from django.shortcuts import render
from projects.models import Project

def project_index(request):
    # Retrieve all objects in projects table
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    # Retrieve project with primary key pk
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
