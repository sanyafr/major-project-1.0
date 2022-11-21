from django.urls import path
from main import views

urlpatterns = [
  path('', views.homepage, name='home'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('login', views.loginpage, name='login'),
  path('logout', views.logoutpage, name='logout'),
  path('register/', views.registerpage, name='register'),
  path('rules/', views.rulespage, name='rules'),
  path('test/', views.testpage, name='test'),
  path('prep/', views.preppage, name='prep'),
  path('companies/', views.companiespage, name='companies'),
  path('students/', views.studentspage, name='students'),
  path('applied_careers/', views.appliedcareers, name='appliedcareers'),
]