from django.db import models
from django.db.models.signals import pre_save
from django.core.validators import MinValueValidator

# Create your models here


class Company(models.Model):
	name 				= models.CharField(max_length=100)
	company_id			= models.PositiveIntegerField(validators=[MinValueValidator(1)], unique=True)

	def __str__(self):
		return self.name


class Medicine(models.Model):
	name 				= models.CharField(max_length=100)
	company 			= models.ForeignKey(Company, on_delete=models.CASCADE)

	def __str__(self):
		return self.name + " - " + self.company.name


class MedicinePacket(models.Model):
	title 				= models.CharField(max_length=100, null=True, blank=True)
	packet_id 			= models.PositiveIntegerField(validators=[MinValueValidator(1)])
	medicine 			= models.ForeignKey(Medicine, on_delete=models.CASCADE)
	manufacturing_date  = models.DateField(null=True, blank=True)
	expiring_date 		= models.DateField(null=True, blank=True)    

	def __str__(self):
		return self.title


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.title or instance.title:
        instance.title = str(instance.packet_id) + " no. packet (" + instance.medicine.name + ") " + instance.medicine.company.name


pre_save.connect(pre_save_receiver, sender=MedicinePacket)