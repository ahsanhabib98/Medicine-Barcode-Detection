from django.db import models
from medicine.models import MedicinePacket
from django.db.models.signals import pre_save
from django.core.validators import MinValueValidator

# Create your models here.

class BarcodeRead(models.Model):
	country_choice = (
			('bangladesh', '1. bangladesh'),
		)

	title 				= models.CharField(max_length=100, null=True, blank=True)
	country 			= models.CharField(max_length=100, choices=country_choice)
	country_id 			= models.PositiveIntegerField(validators=[MinValueValidator(1)])
	company_id 			= models.IntegerField(default=0)
	packet 				= models.OneToOneField(MedicinePacket, on_delete=models.CASCADE)
	details 			= models.TextField()
	details_id 			= models.PositiveIntegerField(validators=[MinValueValidator(1)], unique=True)
	barcode 			= models.CharField(max_length=100, null=True, blank=True)
	scanning 			= models.BooleanField(default=False)
	scanning_id 		= models.IntegerField(default=0)

	def __str__(self):
		return "Barcode of " + str(self.packet.packet_id) + " no. packet (" + self.packet.medicine.name + ") is " + self.barcode


def pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.company_id or not instance.company_id:
        instance.company_id = instance.packet.medicine.company.company_id

    if not instance.title or instance.title:
        instance.title = "Barcode of " + str(instance.packet.packet_id) + " no. packet (" + instance.packet.medicine.name + ") is " + str(instance.barcode)
    
    temp = ""
    if not instance.barcode or instance.barcode:
        if instance.country_id<10:
            temp += "00" + str(instance.country_id) + " "
        elif instance.country_id<100:
            temp += "0" + str(instance.country_id) + " "
        else:
            temp += str(instance.country_id) + " "

        if instance.company_id<10:
            temp += "00" + str(instance.company_id) + " "
        elif instance.company_id<100:
            temp += "0" + str(instance.company_id) + " "
        else:
            temp += str(instance.company_id) + " "

        if instance.details_id<10:
            temp += "0000" + str(instance.details_id) + " "
        elif instance.details_id<100:
            temp += "000" + str(instance.details_id) + " "
        elif instance.details_id<1000:
            temp += "00" + str(instance.details_id) + " "
        elif instance.details_id<10000:
            temp += "0" + str(instance.details_id) + " "
        else:
            temp += str(instance.details_id) + " "
        temp += str(instance.scanning_id)
        instance.barcode = temp


pre_save.connect(pre_save_receiver, sender=BarcodeRead)