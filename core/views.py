from django.shortcuts import render
from .models import Kamar
# File: core/views.py
# Tugas: Mengambil data dari database dan mengirimkannya ke template HTML.



def landing_page(request):
    # Mengambil semua objek kamar dari database
    semua_kamar = Kamar.objects.all().order_by('nomor_kamar')
    
    # Data yang akan dikirim ke template
    context = {
        'daftar_kamar': semua_kamar,
        'jumlah_kamar': semua_kamar.count(),
    }
    
    # Merender halaman HTML dengan data yang sudah disiapkan
    return render(request, 'core/index.html', context)
