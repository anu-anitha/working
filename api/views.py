from django.shortcuts import render
from RestaurantApp.models import Delivery, Table,Skyvy
from AccountsApp.models import CustomUser as User
from BotsApp.models import Bot
from rest_framework.decorators import api_view
from RestaurantApp.models import Table
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

# Create your views here.

#... All Deliveries  ....................
@api_view(['GET'])
def AllDeliveriesView(request):
    data = Delivery.objects.all()
    serializer = DeliverySerializer(data, many = True)
    return Response(serializer.data)


#... latest Delivery  ...................
@api_view(['GET'])
def LatestDeliveryView(request):
    data = Delivery.objects.latest('pk')
    serializer = DeliverySerializer(data, many = False)
    return Response(serializer.data)

#... UPDATE BOT AVAILABILITY ............
@api_view(['POST'])
def BotStatusView(request, id):
    b = Bot.objects.get(id = id)
    serializer = BotStatusSerializer(instance = b, data = request.POST)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#... UPDATE BOT BATTERY..................
@api_view(['POST'])
def BotBatteryView(request, id):
    b = Bot.objects.get(id = id)
    serializer = BotBatterySerializer(instance = b, data = request.POST)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    


#... UPDATE TABLE AVAILABILTIY...........
@api_view(['POST'])
def TableStatusView(request, id):
    t = Table.objects.get(id = id)
    serializer = TableSerializer(instance = t, data = request.POST)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#... UPDATE FOOD DELIVERY STATUS..........
@api_view(['POST'])
def DeliveryStatusView(request, id):
    d = Delivery.objects.get(id = id)
    serializer = DeliveryStatusSerializer(instance = d, data = request.POST)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#... Restaurant Based lates Data..........
@api_view(['GET'])
def RestLatestView(request, username):
    user = User.objects.get(username = username)
    d = Delivery.objects.filter(username = username).latest('pk')
    serializer = DeliverySerializer(d, many = False)
    return Response(serializer.data)


@api_view(['GET'])
def Table_View(request):
    if request.method == 'GET':
        data = Table.objects.latest('pk')
        serializer = Table1Serializer(data, many=False)
        return Response(serializer.data)

@api_view(['POST'])
def Table1_View(request):
    serializer = Table1Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def PostSkyvy(request):
    serializer=SkyvySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def GetSkyvy(request):
    data =Skyvy.objects.latest('pk')
    serializer = SkyvySerializer(data, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def  x(request):
    














