from django.core.exceptions import ObjectDoesNotExist
from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from pip._vendor.requests import Response

from board.models import Board


def home(request):
    rsBoard = Board.objects.all()
    return render(request, "home.html", {'rsBoard': rsBoard})


def board(request):
    rsBoard = Board.objects.all()
    return render(request, "board_list.html", {'rsBoard': rsBoard})


def board_view(request):
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)
    return render(request, "board_view.html", {'rsDetail': rsDetail})


def board_edit(request):
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)
    return render(request, "board_edit.html", {'rsDetail': rsDetail})


def board_update(request):
    bno = request.GET['b_no']
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    try:
        board = Board.objects.get(b_no=bno)
        if btitle != "":
            board.b_title = btitle
        if bnote != "":
            board.b_note = bnote
        if bwriter != "":
            board.b_writer = bwriter
        try:
            board.save()
            return redirect("/board")
        except ValueError:
            return Response({"success": False, "msg": "에러입니다."})
    except ObjectDoesNotExist:
        return Response({"success": False, "msg": "게시글을 찾을 수 없습니다"})

def board_write(request) :
    return render(request, "board_write.html",)

def board_insert(request):
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    if btitle != "":
        rows = Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter)
        return redirect("/board")
    else:
        return redirect("/board_insert")

def board_delete(request) :
    bno = request.GET['b_no']
    rows = Board.objects.get(b_no=bno).delete()
    return redirect("/board")

def rpa(request) :
    return render(request, "rpa.html")