from django.shortcuts import render
from .models import *
from django.http import JsonResponse
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

    if len(keys) == 0 :
        keys = False

    args['fm'] = fm
    args['pts'] = parthers
    args['keys'] = keys

    return render(request, "index.html",args)

def aboyt_keus(request,slug):

    print(Keys.objects.filter(slug= slug)[0])
    return render(request, "index.html")

def nevs(request):

    arg = dict()
    arg['news'] = Nevs.objects.filter(available= True)

    return render(request, "news.html",arg)

def add_zap(request):

    try:
        zai = Zaiavki()

        zai.name = request.GET.get('name')
        zai.svaz = request.GET.get('svaz')
        zai.description = request.GET.get('opis')
        zai.status = "Непрочитанно"
        zai.available = True

        zai.save()

        return JsonResponse({"flag":True})
    except:

        return JsonResponse({"flag": False})