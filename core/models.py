from django.db import models
from django.utils import timezone
# Create your models here.
# File: core/models.py
# Tugas: Mendefinisikan struktur tabel database untuk Kamar dan Penyewa.


class Kamar(models.Model):
    STATUS_CHOICES = [
        ('tersedia', 'Tersedia'),
        ('terisi', 'Terisi'),
        ('perbaikan', 'Dalam Perbaikan'),
    ]
    
    foto_kamar = models.ImageField(
        upload_to='kamar_photos/', 
        null=True, 
        blank=True, 
        help_text="Unggah foto utama kamar"
    )
    
    nomor_kamar = models.CharField(max_length=20, unique=True, help_text="Nomor atau kode unik kamar, misal: 'A01' atau 'B07'")
    lantai = models.CharField(max_length=20, help_text="Posisi lantai, misal: 'Lantai 1' atau 'Bawah'")
    deskripsi = models.TextField(blank=True, null=True)
    harga_per_bulan = models.DecimalField(max_digits=10, decimal_places=2, default=700000.00)
    status_ketersediaan = models.CharField(max_length=15, choices=STATUS_CHOICES, default='tersedia')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Kamar {self.nomor_kamar} - {self.get_status_ketersediaan_display()}"

    class Meta:
        verbose_name_plural = "Daftar Kamar"


class Penyewa(models.Model):
    kamar = models.OneToOneField(Kamar, on_delete=models.SET_NULL, null=True, blank=True, related_name='penyewa_saat_ini')
    nama_lengkap = models.CharField(max_length=150)
    nomor_telepon = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    tanggal_mulai_sewa = models.DateField(default=timezone.now)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nama_lengkap

    class Meta:
        verbose_name_plural = "Daftar Penyewa"

