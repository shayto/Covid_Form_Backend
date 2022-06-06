# Generated by Django 4.0.4 on 2022-05-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('PatientsId', models.AutoField(primary_key=True, serialize=False)),
                ('PatientsFirstName', models.CharField(max_length=30)),
                ('PatientsLastName', models.CharField(max_length=30)),
                ('PatientsBirthday', models.DateField()),
                ('PatientsAddress', models.IntegerField()),
                ('PatientsCity', models.CharField(max_length=30)),
                ('PatientsZipCode', models.IntegerField()),
                ('PatientsLandline', models.IntegerField()),
                ('PatientsCellularPhone', models.IntegerField()),
                ('PatientsBeenInfected', models.BooleanField()),
                ('PatientsPrevConditions', models.BooleanField()),
                ('PatientsOther', models.CharField(max_length=30)),
            ],
        ),
    ]