from django.shortcuts import render
from django.http import *
from .models import *


# Create your views here.
def index(request):
    bookList = bookinfo.objects.all()
    context = {'list': bookList}
    return render(request, 'booktest/index.html', context)


def show(request, id):
    book = bookinfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    context = {'list': herolist}
    return render(request, "booktest/show.html", context)
