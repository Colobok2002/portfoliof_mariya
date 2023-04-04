from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):

    args = dict()

    fm = For_me.objects.filter(avail= True)

    if len(fm) == 0 :
        fm = False
    else:
        fm = fm[0]
    args['fm'] = fm

    parthers = Partners.objects.filter(avail= True)

    if len(parthers) == 0 :
        parthers = False

    keys = Keys.objects.filter(available= True)

    if len(parthers) == 0 :
        keys = False

    args['fm'] = fm
    args['pts'] = parthers
    args['keys'] = keys

    return render(request, "index.html",args)

def aboyt_keus(request,slug):

    print(Keys.objects.filter(slug= slug)[0])
    return render(request, "index.html")

def nevs(request):

    return render(request, "news.html")