from django.shortcuts import redirect, render
from.import models

def index(request):
    if request.POST:
        models.makanan.objects.create(
            nama= request.POST ['nama'],
            jenis= request.POST ['jenis'],
            harga= request.POST ['harga']
            )
        return redirect('/')
    data2 = models.makanan.objects.all()
    return render(request, 'index.html', {
        'isi':data2
        })

def delete(request,id):
    models.makanan.objects.filter(pk=id).delete()
    return redirect ('/')
    
def detail(request,id):
    detail = models.makanan.objects.filter(pk=id).first()
    return render (request,'detail.html', {
        'data': detail,
    })
def update(request,id):
    models.makanan.objects.filter(pk=id).update()
    return render (request,'edit.html')
    