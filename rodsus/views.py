from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
     title='طريق النجاح'
     return render(request,'main.html',{'title':title})
def app(request):
     title='تطبيقي'
     return render(request,'applied.html',{'title':title})
def bio(request):
     title='احيائي'
     return render(request,'biological.html',{'title':title})

def lit(request):
     title='ادبي'
     return render(request,'lit.html',{'title':title})
def cen(request):
     title='دليل الطالب للقبول المركزي'
     return render(request,'cen.html',{'title':title})



