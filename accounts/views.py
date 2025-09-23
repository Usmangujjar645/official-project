

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.core.mail import send_mail
import random



from django.shortcuts import render, redirect

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student, Course
from .forms import StudentForm, CourseForm

# ---------------- Courses ----------------
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html", {"courses": courses})

@login_required
def course_add(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added.")
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "course_form.html", {"form": form})

@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    messages.success(request, "Course deleted.")
    return redirect("course_list")


# ---------------- Students ----------------
@login_required
def student_list(request):
    print("Hello")
    students = Student.objects.all()
    # print(sttud)
    return render(request, "student_list.html", {"students": students})

# @login_required
# def student_add(request):
#     if request.method == "POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Student added.")
#             return redirect("student_list")
#     else:
#         form = StudentForm()
#     return render(request, "student_form.html", {"form": form})



@login_required
def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            roll = form.cleaned_data.get("roll")
            # Check if roll already exists
            if Student.objects.filter(roll=roll).exists():
                messages.error(request, f"Roll number {roll} already exists!")
            else:
                form.save()
                messages.success(request, "Student added successfully.")
                return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "student_form.html", {"form": form})
@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, "Student deleted.")
    return redirect("student_list")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("profile")   # ✅ profile page redirect
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")   # ✅ login page


# ---------------- REGISTER ---------------- #
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")

        # ✅ User create
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully! Please login.")
        return redirect("login")   # Register ke baad login page pe bhej do

    return render(request, "register.html")


# ---------------- PROFILE + INDEX ---------------- #
@login_required
def profile_view(request):
    return render(request, "profile.html")


def index_view(request):
    return render(request, "index.html")




# ---------------- OTP RESET SYSTEM ---------------- #
OTP_STORE = {}


def send_otp(request, *args, **kwargs):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            otp = random.randint(1000, 9999)
            OTP_STORE[email] = otp
            request.session["reset_email"] = email

            # Console me print
            print(f"OTP for {email} is {otp}")

            # Email bhejna
            send_mail(
                subject="Your OTP Code",
                message=f"Your OTP code is {otp}",
                from_email="mani@mail.com",
                recipient_list=[email],
                fail_silently=False,
            )

            messages.success(request, "OTP sent! Check your email.")
            return redirect("verify-otp")

        except User.DoesNotExist:
            messages.error(request, "Email not found")
            return redirect("send-otp")

    return render(request, "reset.html")   # GET request ke liye


class VerifyOtpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "verify-otp.html")

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        verify_otp = request.POST.get("verify-otp")

        real_otp = OTP_STORE.get(email)

        # ✅ type casting zaroori hai
        if real_otp and str(verify_otp) == str(real_otp):
            del OTP_STORE[email]   # otp remove after success
            messages.success(request, "OTP verified! Now set a new password.")
            return redirect("set-new-password")
        else:
            messages.error(request, "Invalid OTP or Email.")
            return render(request, "verify-otp.html")


def set_new_password(request, *args, **kwargs):
    if request.method == "POST":
        email = request.session.get("reset_email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            try:
                user = User.objects.get(email=email)
                user.set_password(password1)
                user.save()
                messages.success(request, "Password reset successfully! Please login.")
                return redirect("login")
            except User.DoesNotExist:
                messages.error(request, "User not found.")
                return redirect("reset-password")
        else:
            messages.error(request, "Passwords do not match")

    return render(request, "set-new-password.html")


def reset_request(request):
    return render(request, "reset.html")



@login_required
def about_view(request):
    return render(request, "about.html")
