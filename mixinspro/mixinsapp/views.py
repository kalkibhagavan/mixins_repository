from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework import generics
from .serializers import productserializers
from .models import product

class productlist(mixins.ListModelMixin,
                  mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = product.objects.all()
    serializer_class = productserializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class productdetails(mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = product.objects.all()
    serializer_class = productserializers

    def get(self,request,pk):
        return self.retrieve(request)

    def put(self,request,pk):
        return self.update(request)

    def delete(self,request,pk):
        return self.destroy(request)