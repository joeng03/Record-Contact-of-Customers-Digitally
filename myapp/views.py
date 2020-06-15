from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages 
from django.urls import reverse
import os
import pandas as pd
from .scraper import write_to_csv

def index(request):
	if "GET" == request.method:
		return render(request,'index.html')
	rows_list=[]
	if request.FILES.get('file').name=='message_1.html':
		write_to_csv(file,rows_list)
	df=pd.DataFrame(rows_list)
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="Data.csv"'
	df.to_csv(path_or_buf=response,index=False)
	return response











