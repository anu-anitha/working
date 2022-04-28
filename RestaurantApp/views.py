from django.shortcuts import redirect, render
from .forms import TempDeliveryForm
from RestaurantApp.models import Delivery, Restaurant, Table, TempDelivery,Skyvy
import time
# Create your views here.


#......   SHOWING RESTAURANTS  ...................................................................
def RestListView(request):    
    r = Restaurant.objects.all()
    return render(request, 'rest_list.html', {'r':r})
#..................................................................................................


#......   SHOWING TABLES   ........................................................................
def TableListView(request):
    return render(request, 'RestaurantApp/tables_list.html')    
#..................................................................................................


#......   SELECTING TABLE   .......................................................................
def SelectTableView(request, id):
    #... Fetching delected table details.....
    table =  Table.objects.get(id = id)

    #... Fetch the recent temp object of the rest.....
    t = TempDelivery.objects.filter(restaurant = request.user.rest.rest_name).latest('pk')

    #... updating the table details in TempDelivery object.....
    t.table_no = table.table_no
    t.save()
    return redirect('RestaurantApp:confirm-delivery')
#..................................................................................................

def gif(request):
    
     # return redirect('RestaurantApp:gif-gif1')
    return render(request,'RestaurantApp/gif.html')

def gif1(request):
    return render(request,'RestaurantApp/gif1.html')

#....select foodtype...............................................................................
# def SelectFoodTypeView(request):
#     obj=TempDelivery.objects.latest('pk')
#     form=TempDeliveryForm()
#     if request.method=='POST':
#         form=TempDeliveryForm(request.POST,instance=obj)
#         if form.is_valid():
#             form.save()
#         return redirect('RestaurantApp:confiverrm-deliy')
#     return render(request,'RestaurantApp/foodtype.html',{'form':form})


#... Confirm DElivery details .....................................................................
def ConfirmDetailsVIew(request):
    t = TempDelivery.objects.filter(restaurant = request.user.rest.rest_name).latest('pk')

    if request.method == "POST":
        FD = Delivery.objects.create(
                                       username = t.username,
                                       restaurant = t.restaurant,
                                       bot_id = t.bot_id,
                                       bot_name = t.bot_name,
                                       bot_color = t.bot_color,
                                       table_no = t.table_no,
                                       food_type = t.food_type,
                                    #    speed = t.speed,
                                       port = t.port,
                                       ip = t.ip,
                                       time = time.time()
                                    )
        FD.save()
        S=Skyvy.objects.latest('pk')
        S.tab_no=t.table_no
        S.save()
        t.delete()
        # return redirect('BotsApp:bots-list')
        return redirect('RestaurantApp:gif-gif')
    return render(request, 'RestaurantApp/confirm_delivery.html' ,{'t':t})
#..................................................................................................
# def SkyvyView(request):
#     t=

#... Delivery details .............................................................................
#..................................................................................................
def DeliveryDetailView(request):
    d = Delivery.objects.filter(restaurant = request.user.rest.rest_name).latest('pk')
    return render(request, 'RestaurantApp/delivery_details.html', {'d':d})


#... End deliveries today .........................................................................
def EndTodayView(request):
    d = Delivery.objects.latest('pk')
    d.time = 0
    d.save()

    return redirect('BotsApp:bots-list')
#..................................................................................................