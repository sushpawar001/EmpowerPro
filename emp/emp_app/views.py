from django.shortcuts import render, redirect
from .forms import UserProfileForm, UserProfileEditForm, LoginForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("employee_home")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "emp_app/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect("login")


@login_required
def home(request):
    return render(request, "emp_app/home.html")


@login_required
def employee_create(request):
    if request.method == "POST":
        profile_form = UserProfileForm(request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.save()
            messages.success(request, "Employee Added.")
            return redirect("employee_create")

    else:
        profile_form = UserProfileForm()

    context = {"profile_form": profile_form}
    return render(request, "emp_app/employee_create.html", context)


@login_required
def employee_view(request):
    sort = request.GET.get("sort")
    members = dir(UserProfile)

    if sort in members:
        emp = UserProfile.objects.order_by(sort)
    else:
        emp = UserProfile.objects.all()

    if request.method == "POST" and "delete" in request.POST:
        employee_id = request.POST.get("delete")
        try:
            employee = UserProfile.objects.get(pk=employee_id)
            employee.delete()
            messages.success(request, "Employee deleted.")
        except UserProfile.DoesNotExist:
            pass

    elif request.method == "POST" and "search" in request.POST:
        name = request.POST.get("search")
        try:
            emp = UserProfile.objects.filter(emplyoee_name__startswith=name)
        except UserProfile.DoesNotExist:
            pass

    context = {"emp": emp}
    return render(request, "emp_app/employee_view.html", context)


@login_required
def employee_edit(request, id):
    employee = UserProfile.objects.get(pk=id)

    if request.method == "POST":
        form = UserProfileEditForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_view")
    else:
        form = UserProfileEditForm(instance=employee)

    context = {
        "form": form,
    }

    return render(request, "emp_app/employee_edit.html", context)
