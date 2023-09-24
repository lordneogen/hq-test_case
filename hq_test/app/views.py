from rest_framework import generics
from . import serializers
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from . import serializers
from rest_framework.response import Response
from django.core.paginator import Paginator, Page

# class List_cr_Products(APIView):
    
#     model=Product
#     queryset =  None
#     serializer_class = serializers.SER_CRUD_Persons
    
    
#     def dispatch(self, request, *args, **kwargs):
#         self.queryset=  self.model.objects.all().filter(author=User.objects.get(pk=request.user.id))
#         return super().dispatch(request, *args, **kwargs)
        
    
#     def get_queryset(self):
#         return self.queryset.all()
    
#     def get(self, request, *args, **kwargs):
            
#         serializer = self.serializer_class(data=self.get_queryset(), many=True)
#         if not serializer.is_valid():
#                 return Response(serializer.data,status=200)
#         else:
#                return Response({"error":"Ошибка валидации"},status=500) 
        
#     def post(self, request, *args, **kwargs):
        
#         try:
#             if request.user.is_authenticated:
#                 serializer = self.serializer_class(data=request.data)

#                 if serializer.is_valid():
#                     serializer.save(author=User.objects.get(pk=request.user.id))
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)

#             return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return Response({'error': 'Ошибка'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# class rud_Products(APIView):
    
    
#     model=Product
#     serializer_class = serializers.SER_CRUD_Persons
#     id=None
#     queryset =None
    
    
    
#     def dispatch(self, request, *args, **kwargs):
#         self.id = kwargs.get('id')
#         try:
#             self.queryset = self.model.objects.get(pk=self.id)
#         except:
#             pass
#         return super().dispatch(request, *args, **kwargs)
    
#     def get(self,request, *args, **kwargs):
        
#         if self.queryset==None:
#             return Response({'error':'Нету обьекта'},status=404)
        
#         serializer = self.serializer_class(self.queryset)
#         return Response(serializer.data,status=200)
        
#     def delete(self, request, *args, **kwargs):
        
#         if self.queryset==None:
#             return Response({'error':'Нету обьекта'},status=404)
#         self.queryset.delete()
#         return Response({"result":"Обьект удален"},status=204)
    
#     def put(self, request, *args, **kwargs):
        
#         if self.queryset==None:
#             return Response({'error':'Нету обьекта'},status=404)
#         serializer = self.serializer_class(instance=self.queryset, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#         return Response(serializer.data,status=200)
    
class List_cr_Lessons(APIView):
    
    model=Lessons_status
    queryset =  None
    serializer_class = serializers.SER_CRUD_Persons
    
    
    def dispatch(self, request, *args, **kwargs):
        self.queryset=  self.model.objects.all().filter(user=User.objects.get(pk=request.user.id))
        return super().dispatch(request, *args, **kwargs)
        
    
    def get_queryset(self):
        return self.queryset.all()
    
    def get(self, request, *args, **kwargs):
            
        serializer = self.serializer_class(data=self.get_queryset(), many=True)
        if not serializer.is_valid():
                return Response(serializer.data,status=200)
        else:
               return Response({"error":"Ошибка валидации"},status=500) 
        
    def post(self, request, *args, **kwargs):
        
        try:
            if request.user.is_authenticated:
                serializer = self.serializer_class(data=request.data)

                if serializer.is_valid():
                    serializer.save(author=User.objects.get(pk=request.user.id))
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Ошибка'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class rud_Products(APIView):
    
    
    model=Product
    serializer_class = serializers.SER_CRUD_Persons
    id=None
    queryset =None
    
    
    
    def dispatch(self, request, *args, **kwargs):
        self.id = kwargs.get('id')
        try:
            self.queryset = self.model.objects.get(pk=self.id)
        except:
            pass
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        
        if self.queryset==None:
            return Response({'error':'Нету обьекта'},status=404)
        
        serializer = self.serializer_class(self.queryset)
        return Response(serializer.data,status=200)
        
    def delete(self, request, *args, **kwargs):
        
        if self.queryset==None:
            return Response({'error':'Нету обьекта'},status=404)
        self.queryset.delete()
        return Response({"result":"Обьект удален"},status=204)
    
    def put(self, request, *args, **kwargs):
        
        if self.queryset==None:
            return Response({'error':'Нету обьекта'},status=404)
        serializer = self.serializer_class(instance=self.queryset, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data,status=200)
    