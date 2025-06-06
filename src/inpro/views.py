from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit





this_dir=pathlib.Path(__file__).resolve().parent




def home_view(request,*args,**kwargs):

    return about_view(request,*args,**kwargs)




def about_view(request,*args,**kwargs):
    qs = PageVisit.objects.all()

    page_qs = PageVisit.objects.filter(path=request.path)

    try:
        percent=(page_qs.count()*100/qs.count()),
    except:
        percent=0

    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit": page_qs.count(),
        "percent": percent,
        "total_visit": qs.count()
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)

    return render(request, html_template, my_context)
