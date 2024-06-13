from django.urls import path, include
from .views import view_branch_product, view_group_product
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('branch-product', view_branch_product.BranchProductViewSet)
router.register('group-product', view_group_product.GroupProductViewSet, basename='group-product')
router.register('group-product-generic', view_group_product.GroupProductGenericViewSet, basename='group-generic')
router.register('group-product-generic-list', view_group_product.GroupProductGenericApis, basename='generic-list')

urlpatterns = [
    path('', include(router.urls)),
]
