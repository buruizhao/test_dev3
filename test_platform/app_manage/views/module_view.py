from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_manage.models import Module
from app_manage.forms import ModuleEditForm


@login_required
def list_module(request):
    """模块管理"""
    module_list = Module.objects.all()
    return render(request, "module/list.html", {
        "modules": module_list
    })


@login_required
def add_module(request):
    """ 模块创建"""
    if request.method == 'POST':
        form = ModuleEditForm(request.POST)

        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            remark = form.cleaned_data['remark']
            Module.objects.create(project=project, name=name, remark=remark)

        return HttpResponseRedirect("/manage/module_list/")
    else:
        form = ModuleEditForm()
        return render(request, "module/add.html", {'form': form})


@login_required
def edit_module(request, mid):
    """ 模块修改"""
    if request.method == 'POST':
        form = ModuleEditForm(request.POST)

        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            remark = form.cleaned_data['remark']

            m = Module.objects.get(id=mid)
            m.project = project
            m.name = name
            m.remark = remark
            m.save()

        return HttpResponseRedirect("/manage/module_list/")
    else:
        if mid:
            m = Module.objects.get(id=mid)
            form = ModuleEditForm(instance=m)
        else:
            form = ModuleEditForm()

        return render(request, "module/edit.html", {'form': form, 'id': mid})


@login_required
def del_module(request, mid):
    if request.method == "GET":
        Module.objects.get(id=mid).delete()
        return HttpResponseRedirect("/manage/module_list/")
    else:
        return HttpResponseRedirect("/manage/module_list/")
