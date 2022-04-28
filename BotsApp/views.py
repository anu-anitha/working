from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from BotsApp.models import Bot
from RestaurantApp.models import TempDelivery

# Create your views here.
def BotListView(request):
    # rest=request.user.rest
    bb=Bot.objects.filter(rest=request.user.rest,avialable=True)

    b=bb[0]
    
    if len(bb)==1:
        rest=request.user.rest
        print(rest)

        # default_bot=Bot[0]
        t = TempDelivery.objects.create(
                                    #  rest=request.user.rest,
                                     username = request.user.username,
                                     restaurant = rest.rest_name,
                                     bot_name = b.bot_name,
                                     bot_id = b.id,
                                     bot_color = b.bot_color,
                                     ip = b.ip,
                                     port = b.port,                                      
                                    )
        t.save()
        return redirect('RestaurantApp:table-list')

    else:

        return render(request, 'BotsApp/bots_list.html')

def SelectBotView(request, id):
    #.... fetching objects......
    b = Bot.objects.get(id = id)
    user = request.user.username
    rest = request.user.rest
    color=b.bot_color

    #... Creating Temp delivery.....
    t = TempDelivery.objects.create(
                                    
                                     username = user,
                                     restaurant = rest.rest_name,
                                    
                                     bot_name = b.bot_name,
                                     bot_id = b.id,
                                     bot_color = b.bot_color,
                                     ip = b.ip,
                                     port = b.port,                                      
                                    )
    t.save()

    return render(request,'RestaurantApp/tables_list.html',{'color':color})

