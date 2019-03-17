"""tandp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from employeeData import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from django.conf.urls import url,include

from users import views as user_views
from meadmin import views as admin_views

from employeeData import views as employee_views
from employeeData import functions as employee_functions


urlpatterns = [

    url('admin/', admin.site.urls, name='qw'),
    url(r'^signin/', include('signin.urls')),
    # url('register/', user_views.register, name='register'),
    url('employee_login/', user_views.employee_login, name='employee_login'),
    url('employee_register/', user_views.employee_register, name='employee_register'),
    url('employer_registration/', user_views.employer_registration, name='employer_registration'),
 
    url('employer_login/', admin_views.employer_login, name='employer_login'),
    # url('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url('logout_employee/', user_views.logout_employee, name='logout_employee'),
    url('category_difference_reason/', user_views.category_difference_reason, name='category_difference_reason'),
    url('logout_employer/', admin_views.logout_employer, name='logout_employer'),


    



    url(r'^employeeData/', include('employeeData.urls')),
    url(r'^employeeData_chart/', employee_views.view_chart, name = "employeeData_chart"),
    # url(ur'^employeeData_chart/(?P<date_var>.+)/(?P<token>.+)/', employee_views.view_chart_custom),)
    url(r'^view_chart_custom/', employee_views.view_chart_custom, name="view_chart_custom"),
    #url(r'^predict_next_month_performance/', employee_views.predict_next_month_performance, name = "predict_next_month_performance"),
    
    url(r'^update_graph/', employee_views.update_graph, name = "update_graph"),
    url(r'^update_db/', employee_functions.sync_firebase_data, name = "update_db"),

    url(r'^employeeData_details/', employee_views.read_process_detail, name = "employeeData_details"),
    url(r'^authconnect/', employee_views.authconnect, name = "authconnect"),
    url(r'^create_new_user/', employee_views.create_new_user, name = "create_new_user"),

]
