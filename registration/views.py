from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

# Create your views here.


def signup(request):
	form = SignUpForm(request.POST or None)
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user.set_password(password)
			user.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('home')

	context = {
		'form': form,
	}
	template = 'registration/signup.html'
	return render(request, template, context)
