from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
from app_manage.forms import ProjectForm, ProjectEditForm


# Create your views here.
# @login_required
# def manage(request):
#     """接口管理"""
#     return render(request, "manage.html")

@login_required
def list_project(request):
    """项目管理"""
    # username = request.COOKIES.get('user', '')
    project_list = Project.objects.all()
    return render(request, "project/list.html", {
        "projects": project_list
    })


@login_required
def add_project(request):
    """ 项目创建"""
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            remark = form.cleaned_data['remark']
            status = form.cleaned_data['status']
            Project.objects.create(name=name, remark=remark, status=status)

        return HttpResponseRedirect("/manage/")
    else:
        form = ProjectForm()
        return render(request, "project/add.html", {'form': form})


@login_required
def edit_project(request, pid):
    """ 项目修改"""
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            remark = form.cleaned_data['remark']
            status = form.cleaned_data['status']

            p = Project.objects.get(id=pid)
            p.name = name
            p.remark = remark
            p.status = status
            p.save()

        return HttpResponseRedirect("/manage/")
    else:
        if pid:
            p = Project.objects.get(id=pid)
            form = ProjectEditForm(instance=p)
        else:
            form = ProjectForm()

        return render(request, "project/edit.html", {'form': form, 'id': pid})


@login_required
def del_project(request, pid):
    if request.method == "GET":
        Project.objects.get(id=pid).delete()
        return HttpResponseRedirect("/manage/")
    else:
        return HttpResponseRedirect("/manage/")
