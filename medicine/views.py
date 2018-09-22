from django.shortcuts import render
from .models import Company, Medicine, MedicinePacket

# Create your views here.

def company(request):
	all_company = Company.objects.all()
	context = {
		'all_company': all_company,
	}
	template = 'medicine/company.html'
	return render(request, template, context)


def companywise_medicine(request, id):
	all_medicine = Medicine.objects.filter(company__id=id)
	context = {
		'all_medicine': all_medicine,
	}
	template = 'medicine/medicine.html'
	return render(request, template, context)


def medicinewise_packet(request, id):
	all_packet = MedicinePacket.objects.filter(medicine__id=id)
	context = {
		'all_packet': all_packet,
	}
	template = 'medicine/packet.html'
	return render(request, template, context)
