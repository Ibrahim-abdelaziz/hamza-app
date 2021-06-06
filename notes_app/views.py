from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from .models import Note
from django.contrib import messages
from django.template.loader import get_template
from django.http import HttpResponse
from .script import check_ip
from django.views.generic import View
from notes_app.utlis.pdf import Render
# Create your views here.


def algorithm_analysis(request):
    query_ip = request.GET.get("query_ip")
    query_user = request.GET.get("query_user")
    query_pass = request.GET.get("query_pass")

    # query = request.GET.getlist('myvar')
    if query_ip and query_user and query_pass:
        print(query_ip, query_user, query_pass)
        run_script = check_ip("192.168.1.1", "Randa-114", "1223334444")
        result = run_script.dict()
        print(run_script)
        return Render.render('pdf/pdf.html', result)
    return render(request, "notes.html", context={"userinput": query_ip})














def all_notes(request):
    all_notes = Note.objects.all()
    context = {
        'all_notes' :all_notes ,
    }
    return render(request , 'notes.html' , context)
