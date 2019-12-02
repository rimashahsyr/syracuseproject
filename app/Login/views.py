from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('login')
    
def index(request):
    return render(request, 'Login.html')

