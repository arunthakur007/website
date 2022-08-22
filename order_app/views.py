from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Order
from .models import Profile
from .models import store_information
from .models import store_item
def home(request):
    title = "Welcome"
    paragraph = "Hello, Please use and test this CRUD!!"
    return render(request,'home.html',{"title":title,"paragraph":paragraph})

def create(request):
    if request.method == "POST":
        store=request.POST.get("store")
        items_name = request.POST.get('items_name')
        price = request.POST.get('price')
        total = request.POST.get('total')
        amount = float(price)*float(total) #request.POST.get('amount')
        # print(items_name,price,total,amount)
        ord = Order(store_id=store, items_name=items_name, price=price, total=total, amount=amount, user_id=1)
        ord.save()
        # this code will redirect my page to users
        return HttpResponseRedirect("/users")
    title="contact me"
    paragraph="hello"
    return render(request,'create.html',{"title":title,"paragraph":paragraph})


def reterive(request):
    obj = Order.objects.all()
    obj_profile = Profile.objects.all()
    store = store_information.objects.all()
    obj_store_item = store_item.objects.all()
    print(obj)
    print(obj_profile)
    print(store)
    print(store_item)



    return render(request,'users.html',{"obj":obj,"obj_profile":obj_profile,"store":store,"obj_store_item":obj_store_item})

def update(request,id):
    if request.method == "POST":
        items_name = request.POST.get('items_name')
        price = request.POST.get('price')
        total = request.POST.get('total')
        amount = request.POST.get('amount')
        obj = Order.objects.get(id=id)
        obj.items_name = items_name
        obj.price = price
        obj.total = total
        obj.amount = amount
        obj.save()
        return HttpResponseRedirect("/users")
    obj = get_object_or_404(Order,id=id) #GeeksModel.objects.all().filter(id=id)
    # obj_profile =
    title = "Update"
    paragraph = "Update the record"
    return render(request,'create.html',{"title":title,"paragraph":paragraph,"obj":obj})






