from django.shortcuts import render,redirect,get_object_or_404
from .models import Glasse,Watche
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
    glass = Glasse.objects.all()
    watch = Watche.objects.all()

    context ={
        'glass': glass,
        'watch': watch
    }
    return render(request, 'phoneix/index.html', context)


def contact(request):
    # if request.method == 'POST'
    # contactpost = request.POST.get('contactpost')
    
    return render(request, 'phoneix/contact.html')


def glasses(request):
    glass = Glasse.objects.all()

    context ={
        'glass': glass,
    }
    return render(request, 'phoneix/glasses.html', context)


@login_required
def glass(request,prodname):
    # jel = Glasse.objects.filter(name=prodname).first()
    jel = get_object_or_404(Glasse, name=prodname)

    context ={
        'jell': jel
    }
    return render(request, 'phoneix/glass.html', context)


def watches(request):
    watch = Watche.objects.all()

    context ={
        'watch': watch
    }
    return render(request, 'phoneix/watches.html', context)

@login_required
def watch(request,id):
    jel = Watche.objects.filter(id=id).first()
    jell = get_object_or_404(Watche, pk=id)

    context ={
        'jel': jel,
        'jell': jell
    }
    return render(request, 'phoneix/watch.html', context)


def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect ('index')
        else:
            print(form.errors)
            messages.error(request,'Something went wrong')
            return redirect('register')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'registration/register.html', context)


def logout(request):
    return render(request, 'registration/logout.html')







