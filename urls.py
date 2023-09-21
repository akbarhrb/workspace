from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.home , name='home'),
    path('scout/' ,views.scout , name='scout'),
    path('economy/' ,views.economy , name='economy'),
    path('tasks/' ,views.tasks , name='tasks'),
    path('delete/<int:id>' , views.delete , name ='delete'),
    path('sure/', views.sure , name = 'sure'),
    path('update/<int:id>' , views.update , name='update'),
    path('updateit/<int:id>' , views.updateit , name='updateit'),
    path('dc/' , views.dc , name='dc'),
]