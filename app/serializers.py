# from pyexpat import model
# from rest_framework import serializers
# from .models import Store


# class StoreGetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         exclude = ('id','key','value','created_at')
        
#     def to_representation(self, instance):
#         data =  super().to_representation(instance)
#         data[instance.key]=instance.value
#         return data


# class StorePostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         fields = ['key','value']
        
        