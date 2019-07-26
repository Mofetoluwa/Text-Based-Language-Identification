from django.http.response import *
from django.shortcuts import *
from LangIdenApp.Comparison_function import *
import os
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	if(str(request.method).lower() == 'get'):
		return render(request, 'index.html')
	else:
		user_input = request.POST.get('user_input')
		print('VIEW_LOG', user_input)

		result = compare(user_input)
		return render(request, 'index.html', {
			'result': result,
			'user_value': user_input

		})

	

def __str__(self):
	return self.result.encode('utf8')