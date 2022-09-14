from django.urls import path
from .views import StoreView

urlpatterns = [
    path('values',StoreView.as_view(),name="values"),
]
