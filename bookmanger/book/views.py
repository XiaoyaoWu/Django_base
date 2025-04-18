from django.shortcuts import render

# Create your views here.
"""
视图所谓的视团 其实就是python函数
视图函数有2个要求:
    1. 视图函数的第一个参数就是接收请求,这个请求其实就是 HttpRequest的类对象
"""

from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    # return HttpResponse('逍遥踏千秋')
    # context 理解为将视图中的数据传递给HTML（模版）
    context = {
        'name': '马上双十一,点击有惊喜'
    }
    return render(request, 'book/index.html', context=context)

