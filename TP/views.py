from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        return HttpResponse("hi")
    if "user" in request.session:
    	return render(request, "tp.html", {"user": request.session["user"], "state": 1})
    return render(request, "tp.html", {"state": 0})

def setSession(request):
	request.session['user'] = "sunil"
	return HttpResponse("Session is set")

def deleteSession(request):
	del request.session["user"]
	return HttpResponse("Session is deleted")