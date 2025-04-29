from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit





this_dir=pathlib.Path(__file__).resolve().parent




def home_page_view(request,*args,**kwargs):
    qs=PageVisit.objects.all()

    #page_qs=PageVisit.objects.filter(path=request.path)

    my_title="My Page"
    my_context={
        "page_title":my_title,
        "page_visit":page_qs.count(),
        "total_visit":qs.count()
    }

    path=request.path
    print("path",path)
    html_template="home.html"
    PageVisit.objects.create(path=request.path)

    return render(request,html_template,my_context)




def about_page_view(request,*args,**kwargs):

    my_title="My Page"
    my_context={
        "page_title":my_title,
    }
    html_="""
    <!DOCTYPE html>
    <html lang="en">
    <body>
       <h1> {page_title} anything?</h1>
    </body>
    </html>  
     """.format(**my_context) #page_title=my_title


    return HttpResponse(html_)
