from django.urls import path
from .views import packetwise_barcode



urlpatterns = [
    path('barcode/<int:id>', packetwise_barcode, name='barcode'),
]