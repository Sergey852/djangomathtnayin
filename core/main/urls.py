from django.urls import path
from . import views
urlpatterns = [
    path("", views.math, name="math"),
    path('calculator/', views.calculator, name = "calculator"),
    path('factorial/', views.factorial, name = "factorial"),
    path('fibonacci/', views.fibonacci, name = "fibonacci"),
    path('bin_10/', views.bin_10, name = "bin_10"),


    path("calculator/res/", views.add, name="res"),
    path("factorial/fact/", views.fact, name="fact"),
    path("fibonacci/fib/", views.fib, name="fib"),
    path("bin_10/bin/", views.bin, name="bin")





]