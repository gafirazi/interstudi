from django.shortcuts import render

from .artikel import *

# Create your views here.
def index(request):
  return render(request, 'index_fashion.html')

def tentangpengajar(request):
  return render(request, 'tentangpengajar.html')

def programlainnya(request):
  program_lainnyas = {
    'sekretaris': {
      'title': 'Interstudi Sekretaris',
      'desc': 'Menghasilkan lulusan sekretaris yang dapat melaksanakan tugas-tugas kesekretarisan atau administrasi perkantoran secara profesional, yang memiliki keterampilan berkomunikasi dan beradaptasi di lingkungan kerja, keterampilan komputer dan internet, memiliki pemahaman tentang manajemen, serta memiliki kepribadian dan berperilaku yang baik sesuai etika profesi.'
    },
    'grafis': {
      'title': 'Interstudi Grafis',
      'desc': 'Desain grafis adalah suatu bentuk komunikasi visual yang menggunakan gambar untuk menyampaikan informasi atau pesan seefektif mungkin. Dalam disain grafis, teks juga dianggap gambar karena merupakan hasil abstraksi simbol-simbol yang bisa dibunyikan, disain grafis diterapkan dalam disain komunikasi dan fine art.'
    },
    'interior': {
      'title': 'Interstudi Interior',
      'desc': 'Desain interior adalah Ilmu yang mempelajari perancangan suatu karya seni yang ada di dalam suatu bangunan dan digunakan untuk memecahkan masalah manusia. Salah satu bidang studi keilmuan yang didasarkan pada ilmu desain.'
    },
    'public_relations': {
      'title': 'Interstudi Public Relations',
      'desc': 'Public Relations adalah suatu proses yang berkesinambungan dari usaha manajemen untuk memperoleh good will dan pengertian dari publik pada umumnya, termasuk stake holder internal.'
    },
    'broadcasting': {
      'title': 'Interstudi Broadcasting',
      'desc': 'Pendidikan broadcasting memberikan pengajaran, pedidikan dan pelatihan kepada siswa untuk memasuki dunia lapangan kerja yang sesungguhnya di bidang penyiaran baik radio maupun televisi. Bahkan konsentrasi ini sangat diminati oleh mereka yang berjiwa kreatif di bidang audio visual.'
    },
    'language_center': {
      'title': 'Interstudi Language Center',
      'desc': 'Memiliki kemampuan berbahasa asing menjadi sangat penting, dalam mengantisipasi era globalisasi. Dengan kemampuan berbahasa asing yang baik, sangat mendukung berbagai profesi yang ada. Menyadari hal ini, InterStudi mengembangkan program studi bahasa.'
    },
    'bursa_kerja': {
      'title': 'Interstudi Bursa Kerja',
      'desc': 'Bursa Kerja InterStudi berdiri tahun 2000, menjadi wadah guna menjembatani para alumni InterStudi dengan perusahaan untuk memasuki dunia kerja. Bursa kerja ini sebagai salah satu wadah resmi guna mengaspirasi dan mengevaluasi seberapa banyak jumlah lulusan InterStudi yang terserap oleh perusahaan pencari kerja.'
    },
    'short_course':{
      'title': 'Interstudi Short Course',
      'desc': 'Program Short Course InterStudi di rancang bagi peserta yang ingin menambah wawasan namun memiliki waktu yang terbatas. Dengan lama belajar 2-3 hari, para peserta diharapkan mendapat pemahaman mengenai materi-materi yang sesuai dengan kebutuhannya.'
    }
  }
  return render(request, 'programlainnya.html', {"program_lainnya": program_lainnyas})  

def faq(request):
  return render(request, 'faq.html')  

def artikel(request):
  return render(request, 'artikel.html', {'list_artikel': list_artikel.values()})  

def detailartikel(request, nama_artikel):
  artikel = list_artikel[nama_artikel]
  return render(request, 'detailartikel.html', {'artikel': artikel})  

def eventint(request):
  fashion_show_2015_imgs = [('fashionshow2015_' + str(i) + '.jpeg') for i in range(1,9)]
  fashion_show_2016_imgs = [('fashionshow2016_' + str(i) + '.jpeg') for i in range(1,15)]
  fashion_show_2017_imgs = [('fashionshow2017_' + str(i) + '.jpeg') for i in range(1,20)]
  return render(request, 'eventint.html', {'fashion_show_2015_imgs': fashion_show_2015_imgs, 'fashion_show_2016_imgs': fashion_show_2016_imgs, 'fashion_show_2017_imgs': fashion_show_2017_imgs})  

def eventkeg(request):
  eventkeg_imgs = [('eventkeg_' + str(i) + '.jpeg') for i in range(1,21)]
  return render(request, 'eventkeg.html', {'eventkeg_imgs': eventkeg_imgs})  

def eventsem(request):
  sem2015_imgs = [('seminar2015_' + str(i) + '.jpeg') for i in range(1,21)]
  sem2014_imgs = [('seminar2014_' + str(i) + '.jpeg') for i in range(1,11)]
  sem2016_imgs = [('seminar2016_' + str(i) + '.jpeg') for i in range(1,18)]
  talkshow_imgs = [('talkshow_' + str(i) + '.jpeg') for i in range(1,7)]
  return render(request, 'eventsem.html', {'sem2015_imgs': sem2015_imgs, 'sem2016_imgs': sem2016_imgs, 'sem2014_imgs': sem2014_imgs, 'talkshow_imgs': talkshow_imgs})  

def pendaftaranonline(request):
  return render(request, 'pendaftaranonline.html')  