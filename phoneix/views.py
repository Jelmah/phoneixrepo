
from django.shortcuts import render,redirect,get_object_or_404
from .models import Glasse,Watche,Contactinfo
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
def index(request):
    glass = Glasse.objects.all().filter()[:3]
    watch = Watche.objects.all()[:3]

    context ={
        'glass': glass,
        'watch': watch
    }
    return render(request, 'phoneix/index.html', context)

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        select = request.POST['select']
        order = request.POST['order']
        cancel = request.POST['cancel']

        contactinfo = Contactinfo(name=name,email=email,number=number,order=order,select=select,cancel=cancel)
        contactinfo.save()
        
    return render(request, 'phoneix/contact.html')


def glasses(request):
    glassgla = Glasse.objects.all()

    context ={
        'glassgla': glassgla,
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
            messages.success(request, 'Your registration is successful')
            # form.save()
            # username=form.cleaned_data.get('username')
            # password=form.cleaned_data.get('password1')
            # user = authenticate(username=username,password=password)
            # login(request,user)
            return redirect ('index')
        else:
            # print(form.errors)
            messages.error(request,'Something went wrong')
            return redirect('register')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'registration/register.html', context)


def search(request):
    queryset_list = Glasse.objects.order_by('-shipin_date')
    queryset_list2 = Watche.objects.order_by('-shipin_date')

    if 'keysearch' in request.GET:
        keysearch = request.GET['keysearch']
        if keysearch :
            try:
                queryset_list = queryset_list2.filter(name__icontains=keysearch)
            except:
                queryset_list = queryset_list.filter(name__icontains=keysearch)
    else:
        print('mi o tiiri nkan kan')



    context = {
        'glassgla':queryset_list,
    }
    return render(request, 'phoneix/search.html', context)


def cart(request):
    return render (request, 'phoneix/cart.html')




