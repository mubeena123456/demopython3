#from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Place1


# Create your views here.

#def demo(request):
 #   return HttpResponse("hello world")


#def about(request)
 #   name="kerala"
 #   return render(request,'about.html',{'obj':name})

#def result(request):
#    n1=int(request.GET['num1'])
#    n2=int(request.GET['num2'])
#    result=n1+n2
#    return render(request,'result.html',{'res':result})

def index1(request):
    ob=Place1.objects.all()
    obj=Place.objects.all()
    return render(request,'index1.html',{'obj1':obj,'ob1':ob})


