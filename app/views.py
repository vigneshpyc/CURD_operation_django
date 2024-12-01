from django.shortcuts import render, redirect
from app.models import first_collection
from django.http import HttpResponse
from app.forms import userForms

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to CURD operations</h1>')
def insert(request):
    # data ={
    #     'name':'vignesh',
    #     'age':20,
    # }
    # first_collection.insert_one(data)
    # return HttpResponse('<h1>Data is saved successfully</h1>')
    if request.method == "POST":
        forms  = userForms(request.POST)
        if forms.is_valid():
            Name = forms.cleaned_data['name']
            Age = forms.cleaned_data['Age']

            try:
                first_collection.insert_one({
                    'name':Name,
                    'Age':Age,
                })
                HttpResponse('Data is saved successfully')
                return redirect('insert')
                
            except Exception as e:
                print("Database Error:",e)
                return HttpResponse("Error inserting into the database")                
        else:
            return render(request,'register.html',{'form':forms})
    else:
        forms = userForms()
        return render (request,'register.html',{'form':forms})