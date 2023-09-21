from django.shortcuts import render,redirect
from .models import Tasks,Dc
# Create your views here.
def home(request):
    x={
        "name" : "Home Page",
    }
    return render(request , 'home.html' , x)


def scout(request):
    x={
        "name" : "Scout Page",
    }
    return render(request, 'scout.html' , x)

def economy(request):
    x={
        "name" : "Economy",
    }
    return render(request, 'economy.html' ,x)

def tasks(request):
    x={
        "name" : "Tasks",
        'tase' : Tasks.objects.all()
    }
    tas = request.POST.get('tasks')
    data = Tasks(task = tas)
    if request.method == 'POST':
        data.save()

        
    return render(request, 'tasks.html' ,x)

def dc(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Dc.objects.filter(name__icontains=q)
    else:
        data = Dc.objects.all()

    con = {
            'data' : data,
        }
    return render(request , 'dc.html', con)


def delete(request , id):
    item = Tasks.objects.get(id=id)
    item.delete() 
    return redirect('tasks')
    #return render(request , 'tasks.html')

def sure(request):
    return render(request , 'sure.html') 

def update(request , id):
    item = Tasks.objects.get(id=id)
    return render(request , 'update.html')   
def updateit(request , id):
    item=Tasks.objects.get(id=id)
    item.save()