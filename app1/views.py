from django.shortcuts import render
import pickle
# Create your views here.
def index(request):
    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')

def diabetes_form(request):
    return render(request,'diabetes_form.html')

def diabetes_result(request):
    model=pickle.load(open('app1/Models/diabetes_model.sav','rb'))
    name=request.GET['name']
    age=request.GET['age']
    Gender=request.GET['gender']
    Gender=Gender.lower()
    pregnencies=request.GET['pregnencies']
    glucose=request.GET['glucose']
    bp=request.GET['bp']
    insulin=request.GET['insulin']
    skinthickness=request.GET['skinthickness']
    bmi=request.GET['bmi']
    dpf=request.GET['dpf']
    x={'m':1,'f':0}
    print(model.predict([[pregnencies,glucose,bp,skinthickness,insulin,bmi,dpf,age]]))
    ans=model.predict([[pregnencies,glucose,bp,skinthickness,insulin,bmi,dpf,age]])
    return render(request,'diabetes_result.html',{'ans':ans[0]})
# def services(request):
#     return render(request,'services.html')

# def contact(request):
#     if request.method=="POST":
#         name = request.POST.get('name')
#         password = request.POST.get('password')
#         contact = Names(name=name,password=password)
#         contact.save()
#     return render(request,'contact.html')

