from django.urls import path

from .views import index, faq, program_studi, galeri, pendaftaran_online, program_lainnya

urlpatterns = [
    path('', index, name="index"),
    path('faq', faq, name="faq"),
    path('program_studi', program_studi, name='program_studi'),
    path('galeri', galeri, name='galeri'),
    path('pendaftaran_online', pendaftaran_online, name='pendaftaran_online'),
    path('program_lainnya', program_lainnya, name='program_lainnya')
]