# Generated by Django 5.0.12 on 2025-02-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sCApp', '0003_remove_doctor_registration_number_remove_patient_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='registration_number',
            field=models.CharField(default='xyz', max_length=100),
        ),
    ]
