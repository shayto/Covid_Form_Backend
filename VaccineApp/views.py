import xlwt

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from VaccineApp.models import CitizenInfo
from VaccineApp.serializers import CitizenSerializer


@csrf_exempt
def citizenApi(request):
    if request.method == 'GET':
        citizen = CitizenInfo.objects.all()
        citizen_serializer = CitizenSerializer(citizen, many=True)
        return JsonResponse(citizen_serializer.data, safe=False)
    elif request.method == 'POST':
        citizen_data = JSONParser().parse(request)
        citizen_serializer = CitizenSerializer(data=citizen_data)
        if citizen_serializer.is_valid():
            citizen_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            print(citizen_serializer.errors)
        return JsonResponse("Failed to Add", safe=False)


@csrf_exempt
def save_file(request):
    human = CitizenInfo.objects.all()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Summary.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Summary')
    row_num = 0

    cols = ['first_name', 'last_name', 'birthdate', 'address',
            'city', 'zip_code', 'landline', 'cell_phone', 'been_infected', 'conditions']

    for col_num in range(len(cols)):
        ws.write(row_num, col_num, cols[col_num])

    rows = human.values_list('first_name', 'last_name', 'birthdate', 'address',
                             'city', 'zip_code', 'landline', 'cell_phone', 'been_infected', 'conditions')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]))

    wb.save(response)
    return response
