from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all() # retrieve information from database
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(), # count number of visits
        "total_visit_count": qs.count()
    }
    path = request.path
    print(path)
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", my_context)