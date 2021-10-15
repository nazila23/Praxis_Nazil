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
        get_makanan = request.POST["makanan"]
        get_minuman = request.POST["minuman"]
        get_jumlah_makanan = request.POST["jumlah_makanan"]
        get_jumlah_minuman= request.POST["jumlah_minuman"]

        input_makanan = models.makanan.objects.filter(id=get_makanan).first()
        input_minuman = models.minuman.objects.filter(id=get_minuman).first()
        models.pesanan.objects.create(nama_makanan = input_makanan, nama_minuman = input_minuman, jumlah_pesanan_makanan=get_jumlah_makanan,jumlah_pesanan_minuman=get_jumlah_minuman)
    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all()
    data = models.pesanan.objects.all()
    return render(request, "pesanan.html", {
        "dataMakanan": dataMakanan,
        "dataMinuman": dataMinuman,
        "data": data,
    })
def deletepesanan(request,id):
    models.pesanan.objects.filter(pk=id).delete()
    return redirect ('pesanan')
    
def detailpesanan(request,id):
    detail = models.pesanan.objects.filter(pk=id).first()
    return render (request,'detail.html', {
        'data': detail,
    })
def updatepesanan(request,id):
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