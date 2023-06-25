from django.shortcuts import render,redirect
from .models import StudentModel
def pnf(request,exception):
    return redirect("uhome")

def fb(request):
    if request.user.is_authenticated and request.method=="POST":
        na=request.user.username
        fb=request.POST.get("")
        try:
            usr=StudentModel.objects.get(name=na)
            return render(request,"fb.html",{"msg":"feedback already submitted"})
        except StudentModel.DoesNotExist:
            data=StudentModel(name=na,feedback=fb)
            data.save()
            return render(request,"fb.html",{"msg":"Thanks For your feedback"})
    elif request.user.is_authenticated:
        return render(request,"fb.html")
    else:
        return redirect("uhome")
        

