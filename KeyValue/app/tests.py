
from ast import Delete
import imp
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from app.models import Store
import json
import requests

class StorListTestCase(APITestCase):

    def setUp(self):
        Store.objects.create(key='key1',value='value1')
        Store.objects.create(key='key2',value='value2')
        Store.objects.create(key='key3',value='value3')
        Store.objects.create(key='key4',value='value4')

    def test_get_list_store(self):
        response_content= {'response': {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}}
        url = reverse('values')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Store.objects.count(), 4)
        self.assertEqual(json.loads(response.content),response_content)
    
    def test_get_empty_list_store(self):
        response_content= {'response': {}} 
        Store.objects.all().delete()
        url = reverse('values')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Store.objects.count(), 0)
        self.assertEqual(json.loads(response.content),response_content)
    
    def test_get_lsit_by_params_store(self):
        url = reverse('values')
        response = self.client.get(url,{'key':'key1,key2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{"response":{"key1":"value1","key2":"value2"}})
        
    def test_post_store(self): 
        url = reverse('values')
        data={'key5':'values5'}
        response = self.client.post(url,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Store.objects.count(), 5)
        self.assertEqual(json.loads(response.content),{'response': 'data created successfully'})
        
    def test_post_error_store(self):
        url = reverse('values')
        data={'key1':'values1'}
        response = self.client.post(url,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Store.objects.count(), 4)
        self.assertEqual(json.loads(response.content),{"errors":"This key key1 is already exixts"})
        
    def test_patch_store(self):
        data={'key1':'updatevalues1','key2':'updatevalues2'}
        url = reverse('values')
        response = self.client.patch(url,data, format='json')        
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        self.assertEqual(json.loads(response.content), {"response":"data update successfully"})
