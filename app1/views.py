from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')

def form1(request):
    return render(request,'form1.html')
# def services(request):
#     return render(request,'services.html')

# def contact(request):
#     if request.method=="POST":
#         name = request.POST.get('name')
#         password = request.POST.get('password')
#         contact = Names(name=name,password=password)
#         contact.save()
#     return render(request,'contact.html')

