# coding=utf-8
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
import datetime
from .models import Event, Brand


@permission_classes([AllowAny])
class BrandList(APIView):
    '''
    비회원일때 api
    GET api/guest/brand_list - 회원가입시 선호브랜드
    - request
    {
        x
    }
    '''
    def get(self, request):
        brands = Brand.objects.filter(category=1).order_by('name')
        brand2 = Brand.objects.filter(category=2).order_by('name')
        brand3 = Brand.objects.filter(category=3).order_by('name')
        brands = brands.union(brand2)
        brands = brands.union(brand3)
        brand = brands.values()
        return JsonResponse({'brand': list(brand)}, status=200)


@permission_classes([AllowAny])
class BrandMain(APIView):
    '''
    비회원일때 api
    POST api/guest/brand_main - 브랜드 메인, 메인페이지의 eventforyou
    - request
    {
        "category_id" : int (category id)
    }
    '''
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        category_id = data['category_id']
        brands = Brand.objects.filter(category=category_id)
        brand = brands.values()
        return JsonResponse({'brand': list(brand)}, status=200)


@permission_classes([AllowAny])
class BrandDetail(APIView):
    '''
    비회원일때 api
    POST api/guest/brand_detail/ - 브랜드 상세
    - request
    {
        "brand_id" : int (brand id)
    }
    '''
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        brand_id = data['brand_id']
        brands = Brand.objects.filter(id=brand_id)
        brand = brands.values()
        return JsonResponse({'brand': list(brand)}, status=200)


@permission_classes([AllowAny])
class EventMain(APIView):
    '''
    비회원일때 api
    POST api/guest/event_main/ - 이벤트 메인
    - request
    {
        "category_id" : int (category id),
        "brand_id" : int array (brand id)
    }
    '''
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        category_id = data['category_id']
        brand_id = data['brand_id']
        events = Event.objects.none()
        if len(brand_id) == 0:
            events = Event.objects.filter(category=category_id)
        else:
            for i in brand_id:
                event = Event.objects.filter(brand=i, category=category_id)
                events = events.union(event)

        event = events.values()
        return JsonResponse({'event': list(event)}, status=200)


@permission_classes([AllowAny])
class EventDetail(APIView):
    '''
    비회원일때 api
    POST api/guest/event_detail/ - 이벤트 상세
    - request
    {
        "event_id" : int (event id)
    }
    '''
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        event_id = data['event_id']
        events = Event.objects.filter(id=event_id)
        event = events.values()
        return JsonResponse({'event': list(event)}, status=200)


@permission_classes([AllowAny])
class EventDeadline(APIView):
    '''
    비회원일때 api
    POST api/guest/event_deadline/ - 브랜드 상세 눌렀을 때 밑에 이벤트들
    - request
    {
        "brand_id" : int (brand id)
    }
    '''
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        brand_id = data['brand_id']
        now = datetime.datetime.now()
        off = Event.objects.filter(brand=brand_id, due__lte=now)
        on = Event.objects.filter(brand=brand_id, due__gt=now)
        off_event = off.values()
        on_event = on.values()
        return JsonResponse({'on_event': list(on_event),
                             'off_event': list(off_event)}, status=200)