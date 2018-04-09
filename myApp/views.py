from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>我是最棒的666</h1> ')

def detail(request,num,num1):
    return HttpResponse('detail-%s-%s'%(num,num1))

from .models import Grades,Students

def grades(request):
    #去模版里取数据
    gradesList = Grades.objects.all()
    #将数据传输给模板，模板渲染页面，将渲染的页面返回给历览器
    return render(request,'myApp/grades.html',{'grades':gradesList})

def students(request):
    studentsList = Students.stuObj.all()
    return render(request,'myApp/students.html',{'students':studentsList})

def studentsNum(request):
    studentsList = Students.stuObj.all()[0:4]
    return render(request,'myApp/students.html',{'students':studentsList})

#分页显示
def stupage(request,page):
    #0-3 3-6
    #page*3
    page = int(page)
    studentsList = Students.stuObj.all()[(page-1)*3:page*3]
    return render(request, 'myApp/students.html', {'students': studentsList})

from django.db.models import Max
def studentSearch(request):
    # studentsList = Students.stuObj.filter(sname__contains='李')
    # studentsList = Students.stuObj.filter(sname__startswith='曾')
    # studentsList = Students.stuObj.filter(pk__in=[2,4])
    # studentsList = Students.stuObj.filter(sage__lt=30)
    # studentsList = Students.stuObj.filter(lastTime__year=2017)
    #描述中带有"刘"这个字的数据时属于哪个班级的
    studentsList = Grades.objects.filter(students__scontend__contains='刘')
    print(studentsList)
    # maxAge = Students.stuObj.aggregate(Max('sage'))
    # print(maxAge)
    # studentsList = Students.stuObj.filter(Q(pk__lt=3) | Q(sage__gt=40))
    return render(request, 'myApp/students.html', {'students': studentsList})

def studentsSex(request):
    # 报异常
    studentsList = Students.stuObj.get(ssex=True)
    # return render(request,'myApp/students.html',{'students':studentsList})
    return HttpResponse('-----')

def gradesStudents(request,num):
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request,'myApp/students.html',{'students':studentsList})

def addstudent(request):
    grade = Grades.objects.get(pk = 2)
    stu = Students.createStudent("李扬",24,True,"我叫李扬，请多关照",grade)
    stu.save()
    return HttpResponse("成功添加")

def addstudent2(request):
    grade = Grades.objects.get(pk = 2)
    stu = Students.stuObj.createStudent("刘开的",44,True,"我叫刘开的，请多关照",grade)
    stu.save()
    return HttpResponse("成功添加")

from django.db.models import F,Q
def gradesAge(request):
    # g = Grades.objects.filter(ggirlnum__gt=F('gboynum')+20)
    # print(g)
    return HttpResponse('*******')