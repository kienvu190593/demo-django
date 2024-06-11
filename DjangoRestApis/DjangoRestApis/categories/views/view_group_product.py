from django.shortcuts import render
from django.http import response
from rest_framework import viewsets, permissions
from rest_framework import serializers
from rest_framework.decorators import action
from categories.models import *
from categories.views.serializers.serializer_group_product import (SerializerGroupProduct)

# Create your views here.

class GroupProductViewSet(viewsets.ModelViewSet):
    queryset = GroupProductTbl.objects.all()
    serializer_class = SerializerGroupProduct
    #permission_classes = []

    @action(methods=['post'], detail=False, url_path='hide-group-1')
    def hide_group(self, request):
        code = request.data.get('code')
        itemExist = GroupProductTbl.objects.filter(code=code).first()

        if itemExist is None:
            raise serializers.ValidationError("làm gì có bản ghi này đâu nhể !")
        else:
            itemExist.objects.update(dlFlg=False)
    
class GroupProductGenericViewSet(viewsets.GenericViewSet):
    queryset = GroupProductTbl.objects.all()
    serializer_class = SerializerGroupProduct
    @action(methods=['post'], detail=True, url_path='hide-group')
    def hide_group(self, request):
        code = request.data.get('code')
        itemExist = GroupProductTbl.objects.filter(code=code).first()

        if itemExist is None:
            raise serializers.ValidationError("làm gì có bản ghi này đâu nhể !")
        else:
            itemExist.objects.update(dlFlg=False)

