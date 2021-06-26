from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core import serializers, exceptions
from .models import User

# Create your views here.
def index(request):
    users = User.objects.order_by('-created_at')
    context = {'users': users}
    return render(request, 'users/index.html', context=context)

def add(request):
    return render(request, 'users/add.html')

def save(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    position = request.POST.get('position')
    image = 'profile/default.jpeg'

    if request.FILES.get('image'):
        image = request.FILES.get('image')

    try:
        check_email = User.objects.get(email=email)
        return render(request, 'users/add.html', { 'error': 'Email address already exists.' })
    except exceptions.ObjectDoesNotExist:
        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.position = position
        user.image = image
        user.save()
        return HttpResponseRedirect('/users')

def detail(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        raise Http404('User does not exist.')
    return render(request, 'users/detail.html' , { 'user': user })

