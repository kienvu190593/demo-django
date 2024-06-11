from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint

# Create your models here.

class User(AbstractUser):
    avata = models.ImageField(upload_to="users/%Y/%m")

class BaseModel(models.Model):
    class Meta:
        abstract = True

    description = models.TextField(max_length=500, null=True, blank=True)
    createDate = models.DateTimeField(auto_created=True)
    updateDate = models.DateTimeField(auto_now=True)
    delFlg = models.BooleanField(default=True)

class BranchProductTbl(BaseModel):
    class Meta:
         db_table = 'branch_product_tbl'
         constraints = [
            UniqueConstraint(fields=['code', 'name'], name='unique_branch_product_code_name')
        ]
         ordering = ['code']
         
    code = models.CharField(max_length=50, null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name
    
class GroupProductTbl(BaseModel):
    class Meta:
        db_table = 'group_product_tbl'
        constraints = [
            UniqueConstraint(fields=['code', 'name'], name='unique_group_product_code_name')
        ]
        ordering = ['code']
    
    code = models.CharField(max_length=50, null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    branch = models.ForeignKey(BranchProductTbl, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class ProductTbl(BaseModel):
    class Meta:
        db_table = 'product_tbl'
        constraints = [
            UniqueConstraint(fields=['code', 'name'], name='unique_product_code_name')
        ]
        ordering = ['code']
    
    code = models.CharField(max_length=50, null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    price = models.FloatField(null=False, blank=False, default=0)
    avatar = models,models.ImageField(upload_to="products/%Y/%m")
    group = models.ForeignKey(GroupProductTbl, on_delete=models.CASCADE)
    
    def __str__(self):
        ProductTbl.objects.get_or_create
        return self.name

class PropertiesTbl(BaseModel):
    class Meta:
        db_table = 'properties_tbl'
        constraints = [
            UniqueConstraint(fields=['code', 'color'], name='unique_properties_code_name')
        ]
    
    code = models.CharField(max_length=50, null=False, blank=False, unique=True)
    color = models.CharField(max_length=50, null=False, blank=False, unique=True)

    products = models.ManyToManyField(ProductTbl)

