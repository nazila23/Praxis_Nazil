from django.core.checks import messages
from django.http import request
from django.http.response import Http404
from django.shortcuts import redirect, render
from.import models

def home(request):
    models.makanan.objects.all()
    return render(request, 'home.html')
#fungsi pesanan
def pesanan(request):
    if request.POST:
        models.pesanan.objects.create(
            np= request.POST ['np'],
            nama= request.POST ['nama'],
            jenis= request.POST ['jenis'],
            harga= request.POST ['harga'],
            )
        return redirect('/pesanan')
    data2 = models.makanan.objects.all()
    data3 = models.minuman.objects.all()
    return render(request, 'pesanan.html', {
        'isi1':data2,
        'isi':data3
        })

def deletepesan(request,id):
    models.pesanan.objects.filter(pk=id).delete()
    return redirect ('pesanan')
    
def detailpesan(request,id):
    detail = models.pesanan.objects.filter(pk=id).first()
    return render (request,'detail.html', {
        'data': detail,
    })
def updatepesan(request,id):
    if request.POST:
        models.pesanan.objects.filter(id=id).update(
            nama= request.POST ['nama'],
            jenis= request.POST ['jenis'],
            harga= request.POST ['harga']
            )
    data = models.pesanan.objects.filter(pk=id).first()
    print(data)
    return render (request,'edit.html',{
        "data": data,
    })

#fungsi makanan
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

def deleteindex(request,id):
    models.makanan.objects.filter(pk=id).delete()
    return redirect ('index')
    
def detailindex(request,id):
    detail = models.makanan.objects.filter(pk=id).first()
    return render (request,'detail.html', {
        'data': detail,
    })
def updateindex(request,id):
    if request.POST:
        models.makanan.objects.filter(id=id).update(
            nama= request.POST ['nama'],
            jenis= request.POST ['jenis'],
            harga= request.POST ['harga'],
            )
    data = models.makanan.objects.filter(pk=id).first()
    print(data)
    return render (request,'edit.html',{
        "data": data,
    })

    #fungsi minuman
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
def deleteminum(request,id):
    models.minuman.objects.filter(pk=id).delete()
    return redirect ('minuman')
    
def detailminum(request,id):
    detail = models.minuman.objects.filter(pk=id).first()
    return render (request,'detail.html', {
        'data': detail,
    })
def updateminum(request,id):
    if request.POST:
        models.minuman.objects.filter(id=id).update(
            nama= request.POST ['nama'],
            jenis= request.POST ['jenis'],
            harga= request.POST ['harga'],
            )
    data = models.minuman.objects.filter(pk=id).first()
    print(data)
    return render (request,'edit.html',{
        "data": data,
    })