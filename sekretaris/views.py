from django.shortcuts import render
from django.http import HttpResponseNotFound  
from .konten_artikel import *
from .konten_program_studi import *
from .konten_program_lainnya import *

# Create your views here.
def index(request):
  return render(request, "index_sekretaris.html", {"program_studis": program_studis})


def artikel(request, nama_artikel):
  content = ""
  print(type(artikels))
  print(len(artikels))
  if nama_artikel in artikels:
    content = artikels[nama_artikel]['content']
    title = artikels[nama_artikel]['title']
    desc = artikels[nama_artikel]['desc']
    img = nama_artikel+".jpg"
    return render(request, "artikel_sekretaris.html", {"content": content, "title": title, "desc": desc, "img": img})
  else:
    return HttpResponseNotFound("404 Not Found")


def hubungi_kami(request):
  return render(request, "hubungi_kami.html")

def pendaftaran_online(request):
  return render(request, "pendaftaran_online_sekretaris.html")

def program_lainnya(request):

  return render(request, 'program_lainnya.html', {"program_lainnya": program_lainnyas})

def program_studi(request, nama_prodi):
  print(nama_prodi, "uy")
  if nama_prodi in program_studis:
    if nama_prodi == "akademi_sekretari":
      return render(request, "akademi_sekretari.html", {"content": program_studis["akademi_sekretari"]})    
    else:
      content = program_studis[nama_prodi]
      is_eksekutif = False
      if nama_prodi == "sekretaris_eksekutif":
        is_eksekutif = True
  return render(request, "program_studi_sekretaris.html", {"content": content, "is_eksekutif": is_eksekutif})


def list_artikel(request):
  return render(request, "list_artikel.html", {"artikels": artikels})

def seminar(request):

  title="Seminar"
  foto_seminar_fashion = ["seminar_fashion_seminar"+str(x)+".jpg" for x in range(1,10)]
  foto_seminar_grooming = ["seminar_grooming_seminar"+str(x)+".jpg" for x in range(1,10)]
  foto_seminar_public_speaking_ags = ["seminar_public_speaking_ags_seminar"+str(x)+".jpg" for x in range(1,10)]
  foto_seminar_public_speaking_okt = ["seminar_public_speaking_okt_seminar"+str(x)+".jpg" for x in range(1,10)]
  foto_seminar_public_speaking_ags2 = ["seminar_public_speaking_ags_2_seminar"+str(x)+".jpg" for x in range(1,10)]
  foto_seminar_public_speaking_feb = ["seminar_public_speaking_feb_seminar"+str(x)+".jpg" for x in range(1,10)]
  foto_seminar_motivasi_sman_17 = ["seminar_motivasi_sman_17_seminar"+str(x)+".jpg" for x in range(1,10)]
  foto_seminar_motivasi_sman_115 = ["seminar_motivasi_sman_115_seminar"+str(x)+".jpg" for x in range(1,10)]
  foto_seminar_motivasi_smkn_59 = ["seminar_motivasi_smkn_59_seminar"+str(x)+".jpg" for x in range(1,10)]

  data = [
    {
      'title': 'Seminar Fashion Adji, Ivan & Billy',
      'date': '21 November 2015',
      'desc': 'Lembaga Pelatihan InterStudi menyelenggarakan seminar Fashion Design dikampus Bulungan guna membantu para siswa SMA/SMK agar dapat menumbuhkan minat untuk mengenal dan belajar tentang fashion. Melalui seminar ini, diharapkan siswa dapat memahami tentang cara berpakaian yang baik, mengkombinasikan warna pakaian, dan penyesuaian jenis pakaian sesuai kegiatannya. Seminar ini dibawakan oleh disainer Indonesia diantaranya, diantaranya Adji Notonegoro, Billy Tjong, dan Ivan Gunawan. atau info lebih lanjut',
      'foto': foto_seminar_fashion
    },
    {
      'title': 'Seminar Personal Grooming Adji Notonegoro',
      'date': '08 Oktober 2016',
      'desc': 'Akademi Sekretari InterStudi melaksanakan seminar personal grooming dikampus Bulungan dalam rangka memberikan pendidikan tentang penampilan seseorang, dimulai dari cara berpakaian sampai dengan tutur kata dan sopan santun. Agar dapat berbusana yang baik, berpenampilan yang rapi, sopan, luwes, serasi dan menarik (personal apperance) sesuai dengan etika dan tata krama pergaulan. Seminar ini dibawakan secara apik oleh pakar disainer Indonesia diantaranya yaitu Adji Notonegoro, Billy Tjong, dan Ivan Gunawan.',
      'foto': foto_seminar_grooming
    },
    {
      'title': 'Seminar Public Speaking M.Farhan',
      'date': '26 Agustus 2017',
      'desc': 'Akademi Sekretari InterStudi menyelenggarakan seminar Public Speaking dikampus Bulungan guna membantu para siswa SMA/SMK untuk dapat menumbuhkan rasa percaya diri dalam berkomunikasi yang dilakukan secara lisan dihadapan banyak orang. Melalui Public Speaking, diharapkan dapat mengetahui pola pikir, gagasan, dan ide-ide luar biasa siswa dimasa depan. Seminar ini dibawakan oleh para ahlinya dibidang komunikasi (presenter), diantaranya M.Farhan, Hilbram Dunar, dan Putra Nababan.',
      'foto': foto_seminar_public_speaking_ags
    },
    {
      'title': 'Seminar Public Speaking Putra Nababan',
      'date': '28 Oktober 2017',
      'desc': '',
      'foto': foto_seminar_public_speaking_okt
    },
    {
      'title': 'Seminar Motivasi SMAN 17',
      'date': '13 Maret 2018',
      'desc': 'Akademi Sekretari InterStudi memberikan seminar motivasi kepada siswa SMA/SMK khususnya kelas XII dalam rangka menghadapi Ujian Akhir dan Ujian Nasional tahun 2018 yang diselenggarakan disekolah. Seminar ini adalah suatu bentuk proses yang menjelaskan intensitas, arah, dan ketekunan belajar siswa agar dapat siap menghadapi ujian dengan mental yang kuat dan raga yang sehat. Tema yang diberikan disesuaikan dengan kebutuhan remaja sekarang, dibawakan oleh Direktur Akademi Sekretari InterStudi: Andhika Yudistira, SE, MIB, MHRM.',
      'foto': foto_seminar_motivasi_sman_17
    },
    {
      'title': 'Seminar Motivasi SMAN 115',
      'date': '16 Maret 2018',
      'desc': 'Akademi Sekretari InterStudi memberikan seminar motivasi kepada siswa SMA/SMK khususnya kelas XII dalam rangka menghadapi Ujian Akhir dan Ujian Nasional tahun 2018 yang diselenggarakan disekolah. Seminar ini adalah suatu bentuk proses yang menjelaskan intensitas, arah, dan ketekunan belajar siswa agar dapat siap menghadapi ujian dengan mental yang kuat dan raga yang sehat. Tema yang diberikan disesuaikan dengan kebutuhan remaja sekarang, dibawakan oleh Direktur Akademi Sekretari InterStudi: Andhika Yudistira, SE, MIB, MHRM.',
      'foto': foto_seminar_motivasi_sman_115
    },
    {
      'title': 'Seminar Motivasi SMKN 59',
      'date': '29 Maret 2018',
      'desc': 'Akademi Sekretari InterStudi memberikan seminar motivasi kepada siswa SMA/SMK khususnya kelas XII dalam rangka menghadapi Ujian Akhir dan Ujian Nasional tahun 2018 yang diselenggarakan disekolah. Seminar ini adalah suatu bentuk proses yang menjelaskan intensitas, arah, dan ketekunan belajar siswa agar dapat siap menghadapi ujian dengan mental yang kuat dan raga yang sehat. Tema yang diberikan disesuaikan dengan kebutuhan remaja sekarang, dibawakan oleh Direktur Akademi Sekretari InterStudi: Andhika Yudistira, SE, MIB, MHRM.',
      'foto': foto_seminar_motivasi_smkn_59
    },
  ]
  return render(request, "seminar.html", {"data": data, "title": title})


def workshop(request):

  title="Workshop"
  desc="Akademi Sekretari InterStudi memberikan workshop Beauty Class dikampus Bulungan dan disekolah tahun 2017. Beauty Class merupakan salah satu kelas yang mempelajari bagaimana cara berpenampilan yang baik dan menarik khususnya bagi siswi kelas XII. Dalam Beauty Class juga diajarkan tentang etika berpenampilan, tidak hanya dari fisik tetapi juga penampilan sikap/manner. Tujuan mempelajari Beauty Class adalah salah satu cara untuk mempercantik wajah dan untuk mempersiapkan diri dalam menghadapi dunia kerja. Pembicara oleh Iman Kretadiasa, sedangkan makeup bekerjasama dengan pihak Oriflame."

  foto_workshop_beauty_sman_33 = ["workshop_beauty_sman_33_workshop"+str(x)+".jpg" for x in range(1,10)]
  foto_workshop_beauty_smkn_62 = ["workshop_beauty_smkn_62_workshop"+str(x)+".jpg" for x in range(1,10)]
  foto_workshop_beauty_smkn_11 = ["workshop_beauty_smkn_11_workshop"+str(x)+".jpg" for x in range(1,10)]
  foto_workshop_beauty_smkn_15 = ["workshop_beauty_smkn_15_workshop"+str(x)+".jpg" for x in range(1,10)]
  foto_workshop_beauty_sman_95 = ["workshop_beauty_sman_95_workshop"+str(x)+".jpg" for x in range(1,10)]

  data = [
    {
      'title': 'BeautyClass SMAN 33',
      'date': '09 Maret 2018',
      'desc': '',
      'foto': foto_workshop_beauty_sman_33
    },
    {
      'title': 'BeautyClass SMKN 62',
      'date': '15 Maret 2018',
      'desc': '',
      'foto': foto_workshop_beauty_smkn_62
    },
    {
      'title': 'BeautyClass SMKN 11',
      'date': '26 Januari 2018',
      'desc': '',
      'foto': foto_workshop_beauty_smkn_11
    },
    {
      'title': 'BeautyClass SMKN 15',
      'date': '27 November 2017',
      'desc': '',
      'foto': foto_workshop_beauty_smkn_15
    },
    {
      'title': 'BeautyClass SMAN 95',
      'date': '02 Februari 2018',
      'desc': '',
      'foto': foto_workshop_beauty_sman_95
    }
  ]
  return render(request, "seminar.html", {"data": data, "title":title, "desc":desc})


