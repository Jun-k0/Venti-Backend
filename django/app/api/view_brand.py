from rest_framework import viewsets
from .models import Brand, SubscribeBrand
from .serializer_brand import BrandSerializer
from django_filters.rest_framework import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend


# 브랜드


class BrandFilter(FilterSet):
    category = filters.NumberFilter(field_name="category")

    class Meta:
        model = Brand
        fields = ['category']


class BrandViewSet(viewsets.ModelViewSet):
    """
        브랜드 목록을 불러오거나 저장/수정/삭제 하는 API
        ---
        # 내용
            - name : 브랜드 이름
            - image : 브랜드 대표 이미지
            - text : 브랜드 설명
            - category : 브랜드가 속한 카테고리(Foreign Key)
    """
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BrandFilter

