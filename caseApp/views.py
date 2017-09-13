from django.shortcuts import render

# Create your views here to put logic 
#   into the app and 
#   request info from model and 
#   pass to template

def publishCase(request):
	  #return render(request, 'caseApp/publishCase.html', {})
      return render(request, 'caseApp/publishCase.html', {})
