from django.shortcuts import render
from django.http import HttpResponse
#from django.shortcuts import render
from htmlapp.models import Students,FilesUpload
from htmlapp.resources import StudentsResource
from django.contrib import messages
from django.db.models import Q
from tablib import Dataset
# Create your views here.
def home(request):
    POST=Students.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        POST=Students.objects.filter(Q(S_id__icontains=q)|Q(S_name__icontains=q)|Q(S_branch__icontains=q))
    else:
        POST=Students.objects.all()
    #POST=classes.objects.filter(C_id="20FE1A1236")
    data={
        'data':POST
    }
    return render(request,'base.html',data)
def simple_upload(request):
    if request.method=='POST':
       file2=request.FILES["file"]
       document=FilesUpload.objects.create(file=file2)
       document.save()
       return HttpResponse("Your file was uploaded")
    return render(request,'upload.html')
