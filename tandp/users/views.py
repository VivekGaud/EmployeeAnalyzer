from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse
from users.forms import *
import json, time
from employeeData.functions import *
from users.models import *
import subprocess, sys, calendar
import os


def employee_register(request):
    if request.method == 'POST':
        form = EmployeeRegForm(request.POST)
        if form.is_valid():
            firebase , auth = init_fcm_auth()
            email = request.POST["email"]
            password = request.POST["password_open"]
            # import pdb; pdb.set_trace()
            try:
                succ_res = auth.create_user_with_email_and_password(email, password)
            except Exception as excp:
                # pdb.set_trace()
                x, y = excp.args
                exp_obj = json.loads(y)
                exception_response = exp_obj["error"]
                return HttpResponse(exception_response["message"])

            else:
                # pdb.set_trace()
                return redirect('employee_login')
                # return HttpResponse(succ_res["localId"] + "-" + succ_res["idToken"])
    else:
        form = EmployeeRegForm()
    return render(request, 'users/register.html', {'form': form})

def employee_login(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = EmployeeDetailsForm(request.POST)
        if form.is_valid():
            if not "email" in request.session:
                email = request.POST["email"]
                password_open = request.POST["password_open"]
                primary_category = request.POST["primary_category"]
                firebase , auth = init_fcm_auth()
                try:
                    succ_res = auth.sign_in_with_email_and_password(email, password_open)
                    pass
                except Exception as excp:
                    x, y = excp.args
                    exp_obj = json.loads(y)
                    exception_response = exp_obj["error"]
                    return HttpResponse(exception_response["message"])

                else:
                    token = succ_res["localId"]
                    request.session["email"] = email
                    request.session["token"] = token
                    emp_login_inst = LoginInstances.objects.create(employeeUID = token)
                    request.session["emp_login_inst"] = emp_login_inst.pk
                    request.session["primary_category_id"] = primary_category
                    primary_category = ProcessCategory.objects.get(pk = primary_category)
                    request.session["primary_category_name"] = primary_category.name

                    request.session["now_time"] = time.ctime(int(emp_login_inst.created_at.timestamp()))

                return render(request, 'users/index.html')

            else:
                
                process_info = process_gathering(request)
                return render(request, 'users/index.html')
        return render(request, 'users/login.html')
    else:
        if 'email' in request.session:
              


            # process_info = process_gathering(request)
            return render(request, 'users/index.html')
        form = EmployeeDetailsForm()



              
    return render(request, 'users/login.html', {'form': form})

def employer_login(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        form = EmployeeDetailsForm(request.POST)
        if form.is_valid():
            emp_obj = EmployeeDetails.objects.filter(email = form.get("email"),is_admin = True, is_deleted = False)
            if len(emp_obj) > 0:
                emp_obj = emp_obj[0]
                passw = form.get("email")
                if emp_obj.password == hashlib.md5(self.passw.encode()).hexdigest():
                    pass
                    # welcome
                else:
                    return HttpResponse('Password Incorrect')
            else:
                return HttpResponse('User doesn\'t exist')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            # run the thread here for every 60 sec update
        return render(request, 'users/index.html')
    else:
        return render(request, 'users/index.html')


def category_difference_reason(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        if "emp_login_inst" in request.session:
            form = CategoryDifferenceReasonForm(request.POST)
            if form.is_valid():
                difference_reason = request.POST["difference_reason"]
                emp_obj = LoginInstances.objects.get(pk = request.session["emp_login_inst"])
                emp_obj.difference_reason = difference_reason
                emp_obj.target_achieved = False
                emp_obj.save()
        return redirect('employee_login')
    else:
        form = CategoryDifferenceReasonForm()
        return render(request, 'users/difference_reason.html',{'form': form})


'''@login_required
def profile(request):
    return render(request, 'users/profile.html')'''

def logout_employee(request):
    redirect_to_reason = False
    # import pdb; pdb.set_trace()
    # if "emp_login_inst" in request.session:
    #     lginstance = LoginInstances.objects.get(pk = request.session["emp_login_inst"])
    #     created_at = timezone.now().date()
    #     today_date_timestamp = calendar.timegm(timezone.now().date().timetuple())
    #     if False and lginstance.created_at.date() == timezone.now().date():
    #         # cat_data = CategoryDataPerDay.objects.filter(created_at = today_date_timestamp, employeeUID =request.session['token'] )
    #         cat_data = CategoryDataPerDay.objects.filter(created_at = today_date_timestamp, employeeUID =request.session['token'] ).exclude(process_category__name = "Others")
    #     else:
    #         pass
    #     if cat_data.count() > 0:
    #         if lginstance.created_at.date() == timezone.now().date():
    #             for a_cat_data in cat_data:
    #                 highest_category_val = 0
    #                 highest_category = None
    #                 if int(a_cat_data.KernelModeTime) > highest_category_val:
    #                     highest_category = a_cat_data.pk

    #         if not highest_category == request.session["primary_category_id"]:
    #             redirect_to_reason = True
    #         else:
    #             redirect_to_reason = False
    try:
        if 'token' in request.session:
            del request.session['token']
        del request.session['email']
        # check for the highest valued category n compare with initial pk to redirect to 'category_difference_reason'
    except KeyError:
        pass
    if redirect_to_reason:
        return redirect('category_difference_reason')
    else:
        return redirect('employee_login')


def employer_registration(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            emp_obj = EmployeeRegister.objects.filter(email = form.get("email"),is_admin = True, is_deleted = False)
            pass
            form.save()
            username = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')

            # run the thread here for every 60 sec update
        return render(request, 'users/login.html')
    else:
        form = EmployeeRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    return redirect('employee_login')


