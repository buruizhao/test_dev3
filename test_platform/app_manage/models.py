from django.db import models

# Create your models here.
class Project(models.Model):
    """项目表"""
    name = models.CharField("名称", max_length=100, null=False, default="")
    remark = models.TextField("备注", default="")
    status = models.BooleanField("状态", default=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.name

class Module(models.Model):
    """模块表"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100, null=False, default="")
    remark = models.TextField("备注", default="")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.name