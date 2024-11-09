from django.urls import path

from .views import index, artikel, hubungi_kami, program_studi, list_artikel, seminar, workshop, pendaftaran_online, program_lainnya

urlpatterns = [
    path('', index, name="index"),
    path('artikel/<str:nama_artikel>', artikel, name="artikel"),
    path('list_artikel', list_artikel, name="list_artikel"),
    path('hubungi_kami', hubungi_kami, name="hubungi_kami"),
    path('program_studi/<str:nama_prodi>', program_studi, name="program_studi"),
    path('seminar', seminar, name="seminar"),
    path('workshop', workshop, name="workshop"),
    path('pendaftaran_online', pendaftaran_online, name="pendaftaran_online"),
    path('program_lainnya', program_lainnya, name="program_lainnya"),
]