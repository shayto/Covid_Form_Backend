from rest_framework import serializers
from VaccineApp.models import CitizenInfo


class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenInfo
        fields = (
            'id', 'first_name', 'last_name', 'birthdate', 'address',
            'city', 'zip_code', 'landline', 'cell_phone', 'been_infected', 'conditions')

