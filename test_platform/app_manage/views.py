from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_manage.models import Project

# Create your views here.
@login_required
def manage(request):
    """
    接口管理
    """
    project_list = Project.objects.all()
    return render(request, "manage.html", {
        "projects":project_list
    })

def add_project(request):
    return render(request, "project_add.html")