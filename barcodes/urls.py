from django.urls import path
from .views import packetwise_barcode, check_barcode



urlpatterns = [
    path('barcode/<int:id>', packetwise_barcode, name='barcode'),
    path('barcode/check', check_barcode, name='checkbarcode'),
]