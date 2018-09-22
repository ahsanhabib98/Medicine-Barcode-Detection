from django.shortcuts import render, get_object_or_404
from .models import BarcodeRead

# Create your views here.


def packetwise_barcode(request, id):
	barcode = get_object_or_404(BarcodeRead, id=id)
	context = {
		'barcode': barcode,
	}
	template = 'barcode/details.html'
	return render(request, template, context)
