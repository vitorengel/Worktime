from django.shortcuts import render
from projects.models import Project

# Create your views here.

def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects_list.html", {
        "projects": projects
    })