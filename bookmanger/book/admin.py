from django.contrib import admin

# Register your models here.
from book.models import BookInfo, PersonInfo
# 注册模型类
admin.site.register(BookInfo)
admin.site.register(PersonInfo)
