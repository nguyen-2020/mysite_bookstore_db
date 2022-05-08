from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .entity import User,Book
def index(request):
    obj = User.objects.all()
    # Books=Book.objects.all()
    context={
        'Users':obj,
        # 'Books':Books,
    }
    return render(request,'users.html',context)