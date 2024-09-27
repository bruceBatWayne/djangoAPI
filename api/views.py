from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from .serializers import profile_serializer
from .models import profile
# Create your views here.

class  profileView(APIView):
     
    serializer_class=serializers.profile_serializer 
    def get(self,request,format=None,pk=None):
        if pk is None:
            profiles=profile.objects.all()
        else:
            profiles=profile.objects.filter(id=pk)
        serializer=self.serializer_class(profiles,many=True)
        return  Response(serializer.data)
     
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save() 
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk):
        profiles=profile.objects.get(id=pk)
        serializer=self.serializer_class(instance=profiles,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def  patch(self,request,pk):
        profiles=profile.objects.get(id=pk)
        serializer=profile_serializer(instance=profiles,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            profiles=profile.objects.get(id=pk)
            return Response(profile_serializer(profiles).data)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        profiles=profile.objects.get(id=pk)
        profiles.delete()
        return Response({"message":f"delete method being called with pk {pk} "})
    
     

     