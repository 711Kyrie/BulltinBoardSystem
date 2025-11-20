from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# 定义视图函数 并且有一个 request 参数
def index(request):
    # 返回纯文本内容
    return HttpResponse("ok")

def login(request):
    # 返回页面对象
    return render(request, "login.html")

def register(request):
    # 重定向到登录页面
    return redirect("/login/")
