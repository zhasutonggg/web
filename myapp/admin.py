from django.contrib import admin
# Register your models here.
from .models import Grades, Students

# 注册
admin.site.register(Grades)
admin.site.register(Students)
#自定义管理页面：
#属性说明
# 列表页属性
#list_display = []  # 显示字段设置
#list_filter = []  # 过滤字段设置
#search_fields = []  # 搜索字段设置
#list_per_page = []  # 分页设置
# 添加，修改页属性
#fields = []  # 规定属性的先后顺序
#fieldsets = []  # 给属性分组 注意：fields与fieldsets不能同时使用
#属性示例：
# 列表页属性
list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
list_filter = ['gname']
search_fields = ['gname']
list_per_page = 5
# 添加，修改页属性
# fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']
fieldsets = [
    ("num", {"fields": ['ggirlnum', 'gboynum']}),
    ("base", {"fields": ["gname", "gdate", "isDelete"]}),
]
#关联对象：需求：在创建一个班级时可以直接添加几个学生


class StudentsInfo(admin.TabularInline):  # 可选参数admin.StackedInline
    model = Students
    extra = 2
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]


#布尔值显示问题示例：

class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    # 设置页面列的名称
    gender.short_description = "性别"
    list_display = ['pk', 'sname', 'sage', gender,
                    'scontend', 'sgrade', 'isDelete']
    list_per_page = 10
#执行按钮位置：


