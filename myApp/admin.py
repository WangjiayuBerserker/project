from django.contrib import admin

# Register your models here.
from .models import Grades,Students

#注册
class StudentsInfo(admin.TabularInline): # 使创建班级时可以创建几个学生(方式：TabularInline【横板】、StackedInline【竖版】)
    model = Students # 哪个模型
    extra = 2   # 创建几个学生


class GradesAdmin(admin.ModelAdmin):
    # 列表页属性
    inlines = [StudentsInfo]    # 加两行，每行是学生
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    # #添加、修改页属性
    # fields = ['gname','gdate','gboynum','ggirlnum','isDelete']
    fieldsets = [
        ('num',{'fields':['gboynum','ggirlnum']}),
        ('base',{'fields':['gname','gdate','isDelete']}),
    ]





admin.site.register(Grades,GradesAdmin)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def sex(self):
        if self.ssex:
            return '男'
        else:
            return '女'


    sex.short_description = '性别'

    def Delete(self):
        if self.isDelete:
            return '是'
        else:
            return '否'


    Delete.short_description = '是否删除'

    def name(self):
        return self.sname

    name.short_description = '姓名'
    # 列表页属性
    list_display = ['pk',name,sex,'sage','scontend','sgrade',Delete]
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 2
    # 执行动作位置
    actions_on_bottom = True
    actions_on_top = False

# admin.site.register(Students,StudentsAdmin)
