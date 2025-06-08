from django.urls import path,include
from . import views
from rest_framework import routers


app_name='newapp'  #namespacing the url
router = routers.SimpleRouter()
router.register(r'students',views.StudentViewSet,basename='student-filter')

urlpatterns = [
    path('', views.index,name='index'),
    path('student/',views.StudenList.as_view(),name='student'),
    path('detail/<int:pk>/',views.DetailList.as_view(),name='detail'),
    path('add/',views.AddStudent.as_view(),name='add'),
    path('edit/<int:pk>',views.EditStudent.as_view(),name='edit'),
    path('delete/<int:pk>',views.DeleteStudent.as_view(),name='delete'),
    path('api/',include(router.urls))
]