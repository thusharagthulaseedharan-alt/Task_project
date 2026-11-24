"""
URL configuration for Taskproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmi/',views.Bmiview.as_view()),
    path('age/',views.Ageview.as_view()),
    path('interest/',views.Simpleinterest.as_view()),
    path('bills/',views.Electricityview.as_view()),
    path('marks/',views.Percentage.as_view()),
    path('discount/',views.Discountview.as_view()),
    path('profit/',views.Profitview.as_view()),
    path('salary/',views.Salaryview.as_view()),
    path('time/',views.Timeview.as_view()),
    path('fuel/',views.Fuelcostview.as_view()),
    path('product/',views.Productview.as_view()),
    path('work/',views.Worksalary.as_view()),
    path('details/',views.Agedetailsview.as_view()),
]
