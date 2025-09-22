
# from django.urls import path
# from . import views


# urlpatterns = [
#      path("login/", views.login_view, name="login"),
# # path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
# path("register/", views.register_view, name="register"),   # ✅
# path("reset/", views.reset_request, name="reset"),
# path("send-otp/", views.send_otp, name="send-otp"),
# path("verify-otp/", views.VerifyOtpView.as_view(), name="verify-otp"),
# path("set-new-password/", views.set_new_password, name="set-new-password"),
# path("profile/", views.profile_view, name="profile"),
       

# ]    

from django.urls import path
from . import views
from .views import VerifyOtpView

urlpatterns = [
        # courses
        path("about/", views.about_view, name="about"),

    path("courses/", views.course_list, name="course_list"),
    path("courses/add/", views.course_add, name="course_add"),
    path("courses/delete/<int:pk>/", views.course_delete, name="course_delete"),

    # students
    path("students/", views.student_list, name="student_list"),
    path("students/add/", views.student_add, name="student_add"),
    path("students/delete/<int:pk>/", views.student_delete, name="student_delete"),

    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path("", views.index_view, name="index"),
    path("send-otp/", views.send_otp, name="send-otp"),
    path("verify-otp/", VerifyOtpView.as_view(), name="verify-otp"),
    path("set-new-password/", views.set_new_password, name="set-new-password"),
]

