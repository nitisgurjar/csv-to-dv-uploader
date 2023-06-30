import csv
from django.shortcuts import render
from django.contrib import messages
from .models import *

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
        else:
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
            for row in csv_data:
                Name = row[0]
                Mobile = row[1]
                Email = row[2]
                Address = row[3]

                Csvv.objects.create(Name=Name, Mobile=Mobile,Email=Email,Address=Address)
            messages.success(request, 'CSV file uploaded successfully.')
    return render(request, 'upload.html')


