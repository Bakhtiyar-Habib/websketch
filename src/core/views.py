from django.shortcuts import render
from .models import Discuss

from .forms import DiscussForm

def discuss_view(request):
	form = DiscussForm()
	if request.method == "POST":
		form = DiscussForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			Discuss.objects.create(**form.cleaned_data)
	
	context = {
    	'form': form
    }
    
	return render(request, "contact.html", context)


# Create your views here.
