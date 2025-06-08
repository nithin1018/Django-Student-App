from django.shortcuts import render,HttpResponse,redirect
from . models import Student
from .forms import StudentForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from . serializers import StudentSerializer
from . filters import StudentFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
def index(request):
    return HttpResponse("Hello i am Nithin")

#FBV
def student_list(request):
    students=Student.objects.all()
    context={
        'students':students,
    }
    return render(request,'newapp/index.html',context)

#CBV
class StudenList(ListView):
    model=Student
    template_name='newapp/student.html'
    context_object_name='students'
    paginate_by=4
    def get_queryset(self):
        student_name=self.request.GET.get('student_name','')
        return Student.objects.filter(name__icontains=student_name)

def detail(request,pk):
    student_detail=Student.objects.get(pk=pk)
    context={
        'student_detail':student_detail,
    }
    return render(request,'newapp/detail.html',context)

class DetailList(DetailView):
    model=Student
    template_name='newapp/detail.html'


def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('newapp:student')
    return render(request,'newapp/add_student.html',{'form':form})

class AddStudent(LoginRequiredMixin, CreateView):
    model=Student
    fields=['name','age','hobby','image']
    template_name='newapp/add_student.html'
    def form_valid(self, form):
        form.instance.user_name=self.request.user
        return super().form_valid(form)


def edit_student(request,pk):
    user=Student.objects.get(pk=pk)
    form=StudentForm(request.POST or None,instance=user)
    if form.is_valid():
        form.save()
        return redirect('newapp:student')
    return render(request,'newapp/edit.html',{'form':form})

class EditStudent(UpdateView):
    model=Student
    fields=['name','age','hobby']
    template_name='newapp/edit.html'

def delete_student(request,pk):
    user=Student.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('newapp:student')
    return render(request,'newapp/delete.html',{'student_detail':user})

class DeleteStudent(DeleteView):
    model=Student
    template_name='newapp/delete.html'
    success_url=reverse_lazy('newapp:student')


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=StudentFilter