from categories.models import GroupProductTbl
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from categories.views.serializers.serializer_branch_product import (SerializerBranchProduct)

class SerializerGroupProduct(ModelSerializer):
    branch = SerializerBranchProduct()
    
    class Meta:
        model = GroupProductTbl
        fields = ['id', 'code', 'name', 'branch', 'createDate']

    def validate_code(self, value):
        if len(value) > 5:
            raise serializers.ValidationError("dài quá rồi cha nội")
        return value
    
    def validate(seft, data):
        groupItem = GroupProductTbl.objects.filter(id=data['id']).first()
        if GroupProductTbl.objects.filter(id=data['id']).exists():
            raise serializers.ValidationError("bản ghi tồn tại rồi ông tướng")
