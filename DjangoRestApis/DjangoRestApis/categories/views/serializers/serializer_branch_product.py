from categories.models import BranchProductTbl
from rest_framework.serializers import ModelSerializer

class SerializerBranchProduct(ModelSerializer):
    class Meta:
        model = BranchProductTbl
        fields = ["id", "code", "name", "createDate", "delFlg"]