from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('sign/', views.sign_up, name='sign-Extreme'),
    path('dashbord/', views.dash, name='dashbord-Extreme'),
    path('login/', views.login, name='login-Extreme'),
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/<int:task_id>/complete/', views.complete_task, name='complete-task'),
    path('w_points/', views.w_points, name='w-points'),
    path('top_user/', views.top_users, name='top-user'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
