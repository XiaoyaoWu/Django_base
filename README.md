## MVC模式说明
M全拼为Model，主要封装对数据库层的访问，对数据库中的数据进行、、改、查作
V全拼为View，用于封装结果，生成页面展示的html内容
C全拼为Controller,用于接收请求,处理业务透辑,与Model和View交互,返回结果

## Django的MVT模式说明
M全拼为Model，与MVC中的M功能相同，负责和数据库交互，进行数据处理
V全拼为View，与MVC中的C功能相同，接收请求，进行业务处理，返回应答
T全拼为Template，与MVC中的V功能相同，负责封装构造要返回的html

## 创建django项目：
django-admin startproject bookmanger
## 运行manage.py文件
cd到bookmanger中 执行python manage.py runserver

## 创建子应用:
cd到bookmanger中 执行python manage.py startapp book 

## 子应用需要注册到工程里面
bookmanger/settings.py 设置里面添加    
'book', # 方案一
'book.apps.BookConfig'  # 方案二

## models.py 创建类，即数据表后需要生成、执行迁移文件
## 生成迁移文件
python manage.py makemigrations
## 执行迁移文件
python manage.py migrate

## 创建超级管理员用户
python manage.py createsuperuser








