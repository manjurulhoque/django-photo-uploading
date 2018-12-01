from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from instaa.models import Photo


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('instaa:login')
    template_name = 'signup.html'


def login_user(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home.html', {})
            else:
                return render(request, 'signin.html', {'error': 'Your account has been disabled'})
        else:
            return render(request, 'signin.html', {'error': 'Invalid login'})
    return render(request, 'signin.html', {})


@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def home(request):
    photos = Photo.objects.all()
    return render(request, 'home.html', {'photos': photos})


@login_required(login_url='/login')
def upload_photo(request):
    if request.method == 'POST':
        new_photo = Photo(title=request.POST['title'], user=request.user, photo=request.FILES['photo'])
        new_photo.save()
        return HttpResponseRedirect(reverse('instaa:home'))
    return render(request, 'upload.html', {})


@login_required(login_url='/login')
def user_photos(request, username=None):
    try:
        user = User.objects.get(username=username)
    except:
        return render(request, 'user_photos.html', {'error': "This user doesn't exists"})

    photos = user.photo_set.all()
    context = {'photos': photos, 'p_user': user}
    return render(request, 'user_photos.html', context)


@login_required(login_url='/login')
def my_photos(request):
    photos = request.user.photo_set.all()
    context = {'photos': photos, 'p_user': request.user}
    return render(request, 'my_photos.html', context)


@login_required(login_url='/login')
def delete_photo(request, id=None):
    photo = Photo.objects.get(id=id)
    photo.delete()
    return redirect('/profile/photos')
