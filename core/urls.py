"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
# urlpatterns = [ 
# path('admin/', admin.site.urls),
# path('accounts/', include('django.contrib.auth.urls')), 
#     path('accounts/', include('accounts.urls')),  # 👈 apna accounts app
#     # path('student/', include('student.urls')),    # 👈 apna student app
#     path('', views.home, name='home'),             
#  ]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('student/', include('student.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('', views.home, name='index'),    # login/logout ke liye
# ]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    # path('admin/', admin.site.urls),

    # # Django built-in auth urls (password reset, change, etc.)
    # path('accounts/', include('django.contrib.auth.urls')),  

    # # Apna accounts app (custom register, login, otp)
    # path('user/', include('accounts.urls')),    

    # # Home page
    # path('', views.home, name='home'),    
    # 
     path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/', include('accounts.urls')),  
#    path('student/', include('student.urls')),   # 👈 student app
    path('', views.home, name='home'),    
      
       
]
