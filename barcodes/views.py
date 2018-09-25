from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import BarcodeRead

# Create your views here.


def packetwise_barcode(request, id):
	barcode = get_object_or_404(BarcodeRead, id=id)
	context = {
		'barcode': barcode,
	}
	template = 'barcode/details.html'
	return render(request, template, context)


def check_barcode(request):
	if request.method == 'POST':
		barcode = request.POST['barcode']
		barcode = str(barcode)
		barcode = barcode[:3] + " " + barcode[3:6] + " " + barcode[6:11] + " " + barcode[11:12]
		try:
			barcode = BarcodeRead.objects.get(barcode=barcode)
			if barcode.scanning == False:
				barcode.scanning = True
				barcode.save()
				context = {
					'barcode': barcode,
				}
				template = 'barcode/check-barcode.html'
				return render(request, template, context)
			else:
				context = {
					'errmsg': 'Already sold'
				}
				template = 'barcode/check-barcode.html'
				return render(request, template, context)
		except (KeyError, BarcodeRead.DoesNotExist):
			context = {
				'errmsg': 'Fake things'
			}
			template = 'barcode/check-barcode.html'
			return render(request, template, context)

	template = 'barcode/check-barcode.html'
	return render(request, template)