from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    # 处理登陆页面
    if request.method == "GET":
        return render(request, "login.html")

    # 处理登陆请求
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return render(request, "login.html", {
                "msg":"用户名或密码不能为空！"
            })

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            #记录用户的登陆状态
            auth.login(request, user)
            return HttpResponseRedirect("/project/")
        else:
            return render(request, "login.html", {
                "msg":"用户名或密码错误！"
            })

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")