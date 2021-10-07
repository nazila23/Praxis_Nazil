# from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from . import models
def index(request):
    if request.POST:
        # data =request.POST['nama']
        # print(data)
        #input data ke database
        models.polls.objects.create(nama = request.POST['nama'])
    # nampilinn daata
    data2 = models.polls.objects.all()
    return render(request, 'index.html', {'isi':data2})

def about(request):
    return HttpResponse("Halaman About")