from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from users.models import *
from meadmin.forms import *

# def registeradmin(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('email')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('loginadmin')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'meadmin/register.html', {'form': form})

def employer_login(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password_open = request.POST["password_open"]
            employer = EmployeeDetails.objects.filter(email = email, is_deleted = False).order_by('-pk')
            
            if employer.count() > 0:
                employer = employer[0]
                if not employer.password == hashlib.md5(password_open.encode()).hexdigest():
                    # messages.error(request, f'Wrong Password')
                    # return redirect('employer_login')
                    return HttpResponse("Password Incorrect")
                if not employer.is_admin:
                    return HttpResponse("You're not an Admin.")
            else:
                messages.error(request, f'User Doesn\'t Exists')
                return redirect('employer_login')
                
            request.session["email"] = email
            return redirect('view_chart_custom')
        else:
            return redirect('employer_login')

    else:
        form = UserRegisterForm()
    return render(request, 'meadmin/loginadmin.html', {'form': form})



def logout_employer(request):
    try:
        del request.session['email']
    except KeyError:
        pass

    return redirect('employer_login')