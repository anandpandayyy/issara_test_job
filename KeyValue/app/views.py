from rest_framework.views import APIView
from .models import Store
from rest_framework.response import Response
from django.db import transaction
from django.utils import timezone
from datetime import timedelta
from rest_framework import status

class StoreView(APIView):
   
    def get_queryset(self,key):
        qs = Store.objects.all()
        if key:
            qs = qs.filter(key__in=key.split(','))
            qs.update(created_at=timezone.now()+timedelta(minutes=5))
        return {i['key']:i['value'] for i in qs.values('key','value')}

    def get(self, request):
        key = request.GET.get('key')
        return Response({"response":self.get_queryset(key)},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = request.data
        with transaction.atomic():
            for k,v in data.items():
                try:
                    Store.objects.create(key=k,value=v)
                except:
                    return Response({'errors':f'This key {k} is already exixts'},status=status.HTTP_400_BAD_REQUEST)        
            return Response({"response":"data created successfully"},status=status.HTTP_201_CREATED)
    
    def patch(self,request):
        data = request.data
        with transaction.atomic():
            for k,v in data.items():
                try:
                    obj=Store.objects.get(key=k)
                    if obj:
                        obj.value=v
                        obj.save()
                                               
                except:
                    return Response({'errors':f'This key {k} does not exixts'},status=status.HTTP_404_NOT_FOUND)        
            return Response({"response":"data update successfully"},status=status.HTTP_205_RESET_CONTENT)
  
        