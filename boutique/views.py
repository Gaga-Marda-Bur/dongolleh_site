from django.shortcuts import render, get_object_or_404
from .models import Bague, BackgroundImage

def accueil(request):
    bagues = Bague.objects.all()
    backgrounds = BackgroundImage.objects.filter(active=True).order_by('order')
    return render(request, 'dongolleh/index.html', {'bagues': bagues,'backgrounds':backgrounds})

def bague_detail(request, pk):
    bague = get_object_or_404(Bague, pk=pk)
    return render(request, 'dongolleh/bague_detail.html', {'bague': bague})
