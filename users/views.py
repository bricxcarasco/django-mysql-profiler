from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core import serializers, exceptions
from django.core.paginator import Paginator
from .models import User

# Create your views here.
def index(request):
    users = User.objects.all().order_by('-created_at')
    paginator = Paginator(users, 5)

    page_number = request.GET.get('page')

    users = paginator.get_page(page_number)

    return render(request, 'users/index.html', {'page_object': users})

def add(request):
    return render(request, 'users/add.html')

def save(request):
    mode = request.POST.get('mode')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    position = request.POST.get('position')
    image = 'profile/default.jpeg'

    if request.POST.get('current_image'):
        image = request.POST.get('current_image')

    if request.FILES.get('image'):
        image = request.FILES.get('image')

    try:
        if mode == 'add' or request.POST.get('current_email') != email:
            check_email = User.objects.get(email=email)

        context = { 'error': 'Email address already exists.' }
        context['user'] = {
            'id': request.POST.get('id'),
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'position': position,
            'image': image
        }
        return render(request, 'users/add.html' if mode == 'add' else 'users/edit.html', context)
    except exceptions.ObjectDoesNotExist:   
        user = User()
        if mode == 'edit':
            user = User.objects.get(pk=request.POST.get('id'))
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

def edit(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        raise Http404('User does not exist.')
    return render(request, 'users/edit.html' , { 'user': user })

def delete(request, id):
    User.objects.filter(pk=id).delete()
    return HttpResponseRedirect('/users')

