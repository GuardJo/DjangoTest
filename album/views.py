import datetime
import os
import random

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from album.models import Album


def album_list(request):
    rsDetail = Album.objects.all()
    return render(request, "album_list.html", {'rsDetail' : rsDetail})

def album_write(request):
    return render(request, "album_write.html")

def album_insert(request):
    atitle = request.POST['a_title']
    atype = request.POST['a_type']
    anote = request.POST['a_note']
    awriter = request.POST['a_writer']

    nameDate = str(datetime.datetime.today().year) + '_' + str(datetime.datetime.today().month) + '_' + str(datetime.datetime.today().day)

    uploadFile = request.FILES['ufile']

    old_name = uploadFile.name
    file_ext = os.path.splitext(old_name)[1]
    new_name = 'A' + nameDate + '_' + str(random.randint(1000000000, 9999999999))

    fs = FileSystemStorage(location='static/board/photo')

    name = fs.save(new_name + file_ext, uploadFile)

    rows = Album.objects.create(a_title=atitle, a_type=atype, a_note=anote, a_image=name, a_writer=awriter)

    return redirect("/album")

def album_view(request):
    ano = request.GET['a_no']
    rsDetail = Album.objects.filter(a_no=ano)
    rsData = Album.objects.get(a_no=ano)
    rsData.a_count = rsData.a_count + 1
    rsData.save()

    return render(request, "album_view.html", {'rsDetail' : rsDetail})

def album_delete(request):
    ano = request.GET['a_no']
    album = Album.objects.get(a_no=ano)
    album.a_usage = 0
    album.save()
    return redirect("/album")

def album_edit(request):
    ano = request.GET['a_no']
    rsDetail = Album.objects.filter(a_no=ano)

    return render(request, "album_edit.html", {'rsDetail' : rsDetail})

def album_update(request):
    ano = request.POST['a_no']
    atitle = request.POST['a_title']
    atype = request.POST['a_type']
    awriter = request.POST['a_writer']
    anote = request.POST['a_note']

    if 'ufile' in request.FILES:
        nameDate = str(datetime.datetime.today().year) + '_' + str(datetime.datetime.today().month) + '_' + str(
            datetime.datetime.today().day)

        uploadFile = request.FILES['ufile']

        old_name = uploadFile.name
        file_ext = os.path.splitext(old_name)[1]
        new_name = 'A' + nameDate + '_' + str(random.randint(1000000000, 9999999999))

        fs = FileSystemStorage(location="static/board/photo")

        name = fs.save(new_name + file_ext, uploadFile)

        album = Album.objects.get(a_no=ano)
        album.a_title = atitle
        album.a_type = atype
        album.a_writer = awriter
        album.a_image = name
        album.a_note = anote
        album.save()

    else :
        album = Album.objects.get(a_no=ano)
        album.a_title = atitle
        album.a_type = atype
        album.a_writer = awriter
        album.a_note = anote
        album.save()

    return redirect("/album")

