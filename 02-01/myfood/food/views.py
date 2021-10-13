from django.core.checks import messages
from django.http import request
from django.http.response import Http404
from django.shortcuts import redirect, render
from.import models

def home(request):
    models.makanan.objects.all()
    return render(request, 'home.html')

def index(request):
    if request.POST:
        models.makanan.objects.create(
            np= request.POST ['np'],
            nama= request.POST ['nama'],
            jenis= request.POST ['jenis'],
            harga= request.POST ['harga'],
            )
        return redirect('/index')
    data2 = models.makanan.objects.all()
    return render(request, 'index.html', {
        'isi':data2
        })

def delete(request,id):
    models.makanan.objects.filter(pk=id).delete()
    return redirect ('index')
    
def detail(request,id):
    detail = models.makanan.objects.filter(pk=id).first()
    return render (request,'detail.html', {
        'data': detail,
    })
def update(request,id):
    if request.POST:
        models.makanan.objects.filter(id=id).update(
            nama= request.POST ['nama'],
            jenis= request.POST ['jenis'],
            harga= request.POST ['harga']
            )
    data = models.makanan.objects.filter(pk=id).first()
    print(data)
    return render (request,'edit.html',{
        "data": data,
    })
def minuman(request):
    if request.POST:
        models.minuman.objects.create(
            np= request.POST ['np'],
            nama= request.POST ['nama'],
            jenis= request.POST ['jenis'],
            harga= request.POST ['harga'],
            )
        return redirect('/minuman')
    data2 = models.minuman.objects.all()
    return render(request,'minuman.html', {
        'isi':data2
        })