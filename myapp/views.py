from django.shortcuts import render
from django.conf import settings
# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("zst is a good man")
from .models import Grades,Students
def grades(request):
                # 去模板里取数据
    gradesList = Grades.objects.all()
                # 将数据传递给模板,模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myapp/grade.html', {"grades": gradesList})
def students(request):
        studentsList = Students.objects.all()
        return render(request, 'myapp/student.html', {"students": studentsList})
def gradesStudents(request,num):
    #获得对应的班级对象
    grade=Grades.objects.get(pk=num)
    #获得班级下的所有学生对象列表
    studentsList=grade.students_set.all()
    return render(request, 'myapp/student.html', {"students": studentsList})

def bp(request):
	return render(request,'myapp/BP.html')
