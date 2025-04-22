from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo,PeopleInfo
# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse("逍遥踏千秋")

# 增加
BookInfo.objects.create(
    name='python入门2',
    pub_date='2010-1-1'
)
# 修改
BookInfo.objects.filter(name='python入门2').update(name='python入门3')

# 删除
BookInfo.objects.filter(name='python入门').delete()

# 查询
BookInfo.objects.get(id=1)
BookInfo.objects.get(pk=2)  # 主键
BookInfo.objects.all()

# 查询编号为1的图书
BookInfo.objects.filter(id__exact=1)

# 查询书名包含'传'的图书 contains：是否包含
BookInfo.objects.filter(name__contains='传')

# 查询书名以'部'结尾的图书 startswith、endswith：以指定值开头或结尾
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书 isnull：是否为null
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书 in：是否包含在范围内
BookInfo.objects.filter(id__in=[1, 3, 5])

# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)

# 查询编号不等于3的图书
BookInfo.objects.exclude(id__exact=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')

################################################
from django.db.models import F,Q
# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gt=F('commentcount'))

# 查询阅读量大于2倍评论量的图书
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)

# 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))

# 查询编号不等于3的图书 Q对象前可以使用~操作符，表示非not
BookInfo.objects.filter(~Q(id=3))

# 聚合函数
from django.db.models import Sum
BookInfo.objects.aggregate(Sum('readcount'))

# 用order_by对结果进行排序
BookInfo.objects.all().order_by('readcount')

# 关联查询
# 查询书籍为1的所有人物信息
book = BookInfo.objects.get(id__exact=1)
book.peopleinfo_set.all()

# 查询人物为1的书籍信息
person = PeopleInfo.objects.get(id__exact=1)
person.book

# 查询图书，要求图书人物为"郭靖"
book = BookInfo.objects.filter(peopleinfo__name='郭靖')

# 查询图书，要求图书中人物的描述包含"八"
book = BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物
people = PeopleInfo.objects.filter(book__name='天龙八部')

# 查询图书阅读量大于30的所有人物
people = PeopleInfo.objects.filter(book__readcount__gt=30)


# all()：返回所有数据。
# filter()：返回满足条件的数据。
# exclude()：返回满足条件之外的数据。
# order_by()：对结果进行排序。

# 1）惰性执行
# 创建查询集不会访问数据库，直到调用数据时，才会访问数据库，调用数据的情况包括迭代、序列化、与if合用
books = BookInfo.objects.all()
for book in books:
    print(book.name)

# 2）缓存
books = BookInfo.objects.all()
[book.id for book in books]
[book.id for book in books]
[book.id for book in books]
# 此方法只会调用一次数据库

# 获取第1、2项，运行查看，不支持负数索引
books = BookInfo.objects.all()[0:2]

# 分页
# 查询数据
books = BookInfo.objects.all()
# 导入分页类
from django.core.paginator import Paginator
# 创建分页实例
paginator = Paginator(books, 2)
# 获取指定页码的数据
page_skus = paginator.page(1)
# 获取分页数据
total_page = paginator.num_pages


