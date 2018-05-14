
from django.urls import path
from .views import reports, Pdf

urlpatterns = [

    path('', reports),
    path('pdf/', Pdf.as_view(), name='print_to_pdf')
]
