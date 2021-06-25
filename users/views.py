from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import User

# Create your views here.
def index(request):
    users = User.objects.order_by('-created_at')
    context = {'users': users}
    return render(request, 'users/index.html', context=context)
