from django.shortcuts import render, redirect
from .models import Proizvod

def homepage(request):
    return render(request, 'homepage.html')

def proizvodi(request):
    proizvodi = Proizvod.objects.all()
    return render(request, 'proizvodi.html', {'proizvodi': proizvodi})

def dodaj_u_kosaricu(request, proizvod_id):
    proizvod = Proizvod.objects.get(id=proizvod_id)
    kosarica = request.session.get('kosarica', {})
    kosarica[proizvod_id] = kosarica.get(proizvod_id, 0) + 1
    request.session['kosarica'] = kosarica
    return redirect('proizvodi')

def kosarica(request):
    kosarica = request.session.get('kosarica', {})
    proizvodi_u_kosarici = []
    ukupna_cijena = 0
    for proizvod_id, kolicina in kosarica.items():
        proizvod = Proizvod.objects.get(id=proizvod_id)
        ukupna_cijena += proizvod.cijena * kolicina
        proizvodi_u_kosarici.append({'proizvod': proizvod, 'kolicina': kolicina})
    return render(request, 'kosarica.html', {'proizvodi_u_kosarici': proizvodi_u_kosarici, 'ukupna_cijena': ukupna_cijena})
