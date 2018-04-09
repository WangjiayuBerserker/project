from django.db import models

# Create your models here.
class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager,self).get_queryset().filter(isDelete = False)
    def createStudent(self,name,age,sex,contend,grade,isD = False):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgrade = grade
        stu.ssex = sex
        stu.scontend = contend
        return stu

class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s'%(self.gname)# 修改显示(重写str)


class Students(models.Model):
    #自定义模型管理器
    stuObj_zero = models.Manager()
    stuObj = StudentsManager()
    sname = models.CharField(max_length=20)
    ssex = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE) # 添加外键，不成TypeError
    def __str__(self):
        return self.sname

    #lastTime = models.TimeField(auto_now=True)
    #createTime = models.TimeField(auto_now_add=True)

    # class Meta:
    #     db_table = "students"
    #     ordering = ["id"]

    #定义一个类方法创建一个对象
    @classmethod
    def createStudent(cls,name,age,sex,contend,grade,isD = False):
        stu = cls(sname=name,sage=age,ssex=sex,scontend=contend,sgrade=grade,isDelete=isD)
        return stu


