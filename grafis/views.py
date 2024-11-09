from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index_grafis.html')

def faq(request):
  return render(request, 'faq_grafis.html')

def program_studi(request):
  return render(request, 'program_studi.html')

def galeri(request):
  list_foto = ['galeri'+str(i)+'.jpg' for i in range(1,3)]
  return render(request, 'galeri.html', {'list_foto': list_foto})

def pendaftaran_online(request):
  return render(request, 'pendaftaran_online.html')

def program_lainnya(request):
  program_lainnyas = {
    'sekretaris': {
      'title': 'Interstudi Sekretaris',
      'desc': 'Menghasilkan lulusan sekretaris yang dapat melaksanakan tugas-tugas kesekretarisan atau administrasi perkantoran secara profesional, yang memiliki keterampilan berkomunikasi dan beradaptasi di lingkungan kerja, keterampilan komputer dan internet, memiliki pemahaman tentang manajemen, serta memiliki kepribadian dan berperilaku yang baik sesuai etika profesi.'
    },
    'fashion_design': {
      'title': 'Interstudi Fashion Design',
      'desc': 'Keindahan juga dapat dimanfaatkan untuk keperluan yang bersifat komersial atau bisnis. Desain yang “berhasil” bahkan membuat orang per orang atau publik memiliki impresi yang tidak mudah terlupakan.'
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
  return render(request, 'program_lainnya.html', {"program_lainnya": program_lainnyas})