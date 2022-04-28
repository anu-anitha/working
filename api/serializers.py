from RestaurantApp.models import Delivery, Table,Skyvy
from BotsApp.models import Bot
from  RestaurantApp.models import Table
from rest_framework import serializers

#...  Delivery Serializers ....................................
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('food_delivered',)
#..............................................................


#...  Bot Serializers .........................................

class BotStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('avialable',)

class BotBatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('battery',)
#..............................................................

#... Table Serializers ........................................
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('avialable',)
#..............................................................

class Table1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('table_no','created_at')

class SkyvySerializer(serializers.ModelSerializer):
    class Meta:
        model=Skyvy
        fields='__all__'