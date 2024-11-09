from django.shortcuts import render

# Create your views here.
def index(request):

  courses = [
    {
      "name": "Akademi Sekretaris",
      "color": "#F074CA",
      "img": "img/sekretaris.png",
      "url": "sekretaris"
    },
    {
      "name": "Fashion Design",
      "color": "#851110",
      "img": "img/fashion.png",
      "url": "fashion"
    },
    {
      "name": "Desain Grafis",
      "color": "#4157FF",
      "img": "img/design_grafis.png",
      "url": "grafis"
    },
    {
      "name": "Language Center",
      "color": "#3E6785",
      "img": "img/language.png",
      "url": ""
    },
    {
      "name": "Interior Design",
      "color": "#D3AF7F",
      "img": "img/interior.png",
      "url": ""
    },
    {
      "name": "Public Relations",
      "color": "#F7B516",
      "img": "img/sekretaris.png",
      "url": "public_relations"
    },
    {
      "name": "Broadcast",
      "color": "#3B9B75",
      "img": "img/broadcast.png",
      "url": ""
    },
    {
      "name": "Short Course",
      "color": "#7D7D7D",
      "img": "img/short_course.png",
      "url": ""
    },
    {
      "name": "Bursa Kerja",
      "color": "#105036",
      "img": "img/job.png",
      "url": ""
    },

  ]

  return render(request, "index.html", {"courses": courses})