from django.urls import path
from. import views
from django.contrib.auth.views import LogoutView
appname='todo'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('share/',views.ShareView.as_view(),name='share'),
    path('task/',views.TaskList.as_view(),name='home'),
    path('task/create/',views.TaskCreateView.as_view(),name='task_create'),
     path('task/login/',views.UserLoginView.as_view(),name='login'),
    path('task/logout/',LogoutView.as_view(next_page='home'),name='logout'),
    path("task/register/",views.UserRegisterView.as_view(),name='register'),
    path('tasks/update/<int:pk>/',views.TaskUpdateView.as_view(),name='task_update'),
    path('tasks/delete/<int:pk>/',views.TaskDeleteView.as_view(),name='task_delete'),
    path('tasks/<int:pk>/',views.TaskDetailView.as_view(),name='task_detail'),
]

