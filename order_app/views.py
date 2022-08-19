from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import order

def home(request):
    title = "Welcome"
    paragraph = "Hello, Please use and test this CRUD!!"
    return render(request,'home.html',{"title":title,"paragraph":paragraph})

def create(request):
    if request.method == "POST":
        items_name = request.POST.get('items_name')
        price = request.POST.get('price')
        total = request.POST.get('total')
        amount = request.POST.get('amount')
        g = order(items_name=items_name,price=price,total=total,amount=amount)
        g.save()
        # this code will redirect my page to users
        return HttpResponseRedirect("/users")
    title="contact me"
    paragraph="hello"
    return render(request,'create.html',{"title":title,"paragraph":paragraph})


def reterive(request):
    obj = order.objects.all()
    print(obj)

    return render(request,'users.html',{"obj":obj})

def update(request,id):
    if request.method == "POST":
        items_name = request.POST.get('items_name')
        price = request.POST.get('price')
        total = request.POST.get('total')
        amount = request.POST.get('amount')
        obj = order.objects.get(id=id)
        obj.items_name = items_name
        obj.price = price
        obj.total = total
        obj.amount = amount
        obj.save()
        return HttpResponseRedirect("/users")
    obj = get_object_or_404(order,id=id) #GeeksModel.objects.all().filter(id=id)
    title = "Update"
    paragraph = "Update the record"
    return render(request,'create.html',{"title":title,"paragraph":paragraph,"obj":obj})
