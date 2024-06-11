from django.shortcuts import render
from django.http import response
from rest_framework import viewsets
from categories.models import *
from categories.views.serializers.serializer_branch_product import (SerializerBranchProduct)
# Create your views here.

class BranchProductViewSet(viewsets.ModelViewSet):
    queryset = BranchProductTbl.objects.all()
    serializer_class = SerializerBranchProduct
