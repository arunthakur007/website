# list1=[1,11,23,44,22,1,23,67,76,44]
# # res={}
# print(len(list1))
# for i in list1:
#     # res[i] = list1.count(i)
#     print(i,'repeated',list1.count(i))

# print(res


# from django.shortcuts import render,HttpResponseRedirect
# from django.shortcuts import get_object_or_404
# from .models import Order
# from .models import Profile
# from .models import store_information
# from .models import store_item
# def home(request):
#     title = "Welcome"
#     paragraph = "Hello, Please use and test this CRUD!!"
#     return render(request,'home.html',{"title":title,"paragraph":paragraph})
#
# def create(request,id):
#     items = store_item.objects.all().filter(store_id=id)
#
#     if request.method == "POST":
#         items_name = request.POST.get('items_name')
#         total = request.POST.get('total')
#         order_status = request.POST.get('order_status')
#         obj_data = items.filter(id=items_name)
#         price = list(obj_data.values())[0].get('price')
#         amount = float(price)*float(total)
#         ord = Order(store_id=id, items_name=items_name, price=price, total=total, amount=amount,order_status=order_status, user_id=1)
#         ord.save()
#         # this code will redirect my page t
#         # o users
#         return HttpResponseRedirect("/users")
#     title="Add Order"
#     paragraph="hello"
#     return render(request,'create.html',{"title":title,"paragraph":paragraph,"store_items":items})
#
# def select_store(request):
#     store_info = store_information.objects.all()
#     if request.method == "POST":
#         store = request.POST.get("store")
#         print(store)
#
#         return HttpResponseRedirect(f"/create/{store}")
#     title="Choose Store"
#     return render(request,'create.html',{"title":title, 'store':store_info})
#
#
#
# def reterive(request):
#     obj = Order.objects.all()
#     obj_profile = Profile.objects.all()
#     store = store_information.objects.all()
#     obj_store_item = store_item.objects.all()
#     print(obj)
#     print(obj_profile)
#     print(store)
#     print(store_item)
#
#
#
#     return render(request,'users.html',{"obj":obj,"obj_profile":obj_profile,"store":store,"obj_store_item":obj_store_item})
#
# def update(request,id):
#     if request.method == "POST":
#         items_name = request.POST.get('items_name')
#         price = request.POST.get('price')
#         total = request.POST.get('total')
#         amount = request.POST.get('amount')
#         obj = Order.objects.get(id=id)
#         obj.items_name = items_name
#         obj.price = price
#         obj.total = total
#         obj.amount = amount
#         obj.save()
#         return HttpResponseRedirect("/users")
#     obj = get_object_or_404(Order,id=id) #GeeksModel.objects.all().filter(id=id)
#     # obj_profile =
#     title = "Update"
#     paragraph = "Update the record"
#     return render(request,'create.html',{"title":title,"paragraph":paragraph,"obj":obj})


# from django.shortcuts import render, HttpResponseRedirect
# from django.shortcuts import get_object_or_404
# from .models import Order
# from .models import Profile
# from .models import store_information
# from .models import store_item
#
#
# def home(request):
#     title = "Welcome"
#     paragraph = "Hello, Please use and test this CRUD!!"
#     return render(request, 'home.html', {"title": title, "paragraph": paragraph})
#
#
# def create(request, id):
#     items = store_item.objects.all().filter(store_id=id)
#
#     if request.method == "POST":
#         items_name = request.POST.get('items_name')
#         total = request.POST.get('total')
#         print(items_name, total)
#         obj_data = items.filter(id=items_name)
#
#         print(obj_data)
#
#         # price = request.POST.get('price')
#         #
#         # amount = float(price)*float(total) #request.POST.get('amount')
#         # print(items_name,price,total,amount)
#         # ord = Order(store_id=id, items_name=items_name, price=price, total=total, amount=amount, user_id=1)
#         # ord.save()
#         # this code will redirect my page to users
#         return HttpResponseRedirect("/create/1")
#     title = "Add Order"
#     paragraph = "hello"
#     return render(request, 'create.html', {"title": title, "paragraph": paragraph, "store_items": items})
#
#
# def select_store(request):
#     store_info = store_information.objects.all()
#     if request.method == "POST":
#         store = request.POST.get("store")
#         print(store)
#
#         return HttpResponseRedirect(f"/create/{store}")
#     title = "Choose Store"
#     return render(request, 'create.html', {"title": title, 'store': store_info})
#
#
# def reterive(request):
#     obj = Order.objects.all()
#     obj_profile = Profile.objects.all()
#     store = store_information.objects.all()
#     obj_store_item = store_item.objects.all()
#     print(obj)
#     print(obj_profile)
#     print(store)
#     print(store_item)
#
#     return render(request, 'users.html',
#                   {"obj": obj, "obj_profile": obj_profile, "store": store, "obj_store_item": obj_store_item})
#
#
# def update(request, id):
#     if request.method == "POST":
#         items_name = request.POST.get('items_name')
#         price = request.POST.get('price')
#         total = request.POST.get('total')
#         amount = request.POST.get('amount')
#         obj = Order.objects.get(id=id)
#         obj.items_name = items_name
#         obj.price = price
#         obj.total = total
#         obj.amount = amount
#         obj.save()
#         return HttpResponseRedirect("/users")
#     obj = get_object_or_404(Order, id=id)  # GeeksModel.objects.all().filter(id=id)
#     # obj_profile =
#     title = "Update"
#     paragraph = "Update the record"
#     return render(request, 'create.html', {"title": title, "paragraph": paragraph, "obj": obj})


name="arun thakur "
print(name.title())



name="arun thakur"

print(name[:name.index(" ")].capitalize())
print(name[name.index(" ")+1:].capitalize())

