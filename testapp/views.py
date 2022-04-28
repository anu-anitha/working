from django.shortcuts import render
from .serialisers import ExitSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Exit

# Create your views here.


@api_view(['GET', 'POST'])
def ApiView(request):
 
    if request.method == 'GET':
        data = Exit.objects.latest("pk")
        serializer = ExitSerializer(data, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ExitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

