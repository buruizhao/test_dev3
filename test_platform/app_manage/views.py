from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
from .forms import ProjectForm, ProjectEditForm


# Create your views here.
@login_required
# def manage(request):
#     """
#     接口管理
#     """
#     return render(request, "manage.html")

def manage(request):
    """
     项目管理
    """
    project_list = Project.objects.all()
    return render(request, "project_list.html", {
        "projects": project_list
    })


def add_project(request):
    """ 项目创建"""
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            remark = form.cleaned_data['remark']
            status = form.cleaned_data['status']
            Project.objects.create(name=name, remark=remark, status=status)

        return HttpResponseRedirect("/project/")
    else:
        form = ProjectForm()
        return render(request, "project_add.html", {'form': form})


def edit_project(request, pid):
    """ 项目修改"""
    print("pid", pid)
    if request.method == 'POST':
        pass
    else:
        if pid:
            p = Project.objects.filter(id=pid)
            form = ProjectEditForm(instance=p)
        else:
            form = ProjectForm()

    return render(request, "project_edit.html", {
        "form": form
    })
