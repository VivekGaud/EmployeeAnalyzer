from __future__ import absolute_import
from celery import shared_task
from reports import generate_report_excel

@shared_task  # Use this decorator to make this a asyncronous function
def generate_report(data_inicial, data_final, email):
    generate_report_excel(
        ini_date = ini_date,
        final_date = final_date,
        email = email
    )