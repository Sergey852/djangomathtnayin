from django.shortcuts import render

# Create your views here.
def math(request):
    return render(request, "math.html")

def calculator(request):
    return render(request, "calculator.html")

def factorial(request):
    return render(request, "factorial.html")

def fibonacci(request):
    return render(request, "fibonacci.html")

def bin_10(request):
    return render(request, "bin_10.html")

def add(request):
    num1 = int(request.POST["num1"])
    num2 = int(request.POST["num2"])
    char = str(request.POST['char'])
    if char == "+":
        res = num1 + num2
    elif char =="-":
        res = num1 - num2
    elif char == "*":
        res = num1*num2
    elif char == "/":
        res = num1/num2
    return render(request, "result.html", {"res":res})

def fact(request):
    n = int(request.POST["n"])
    res = 1
    for i in range(1, n+1):
        res *= i
    return render(request, "fact.html", {"res":res})

def fib(request):
    n = int(request.POST["n"])
    if n ==0:
        res = 0
    if n == 1 or n ==2:
        res = 1
    else:
        res = fib(n-2) + fib(n-1)
    return render(request, "fib.html", {"res":res})

def bin(request):
    n = request.POST["n"]
    res = int(n, 2)
    return render(request, "bin.html", {"res":res})


