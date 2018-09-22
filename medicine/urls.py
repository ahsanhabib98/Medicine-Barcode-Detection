from django.urls import path
from .views import company, companywise_medicine, medicinewise_packet



urlpatterns = [
    path('company/', company, name='company'),
    path('medicine/<int:id>/', companywise_medicine, name='medicine'),
    path('packet/<int:id>/', medicinewise_packet, name='packet'),
]