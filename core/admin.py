from django.contrib import admin
# File: core/admin.py
# Tugas: Mendaftarkan model ke Panel Admin bawaan Django.
from .models import Kamar, Penyewa

@admin.register(Kamar)
class KamarAdmin(admin.ModelAdmin):
    list_display = ('nomor_kamar', 'lantai', 'harga_per_bulan', 'status_ketersediaan', 'updated_at')
    list_filter = ('status_ketersediaan', 'lantai')
    search_fields = ('nomor_kamar',)
    ordering = ('nomor_kamar',)
    list_editable = ('harga_per_bulan', 'status_ketersediaan')
    fieldsets = (
        (None, {
            'fields': ('nomor_kamar', 'lantai', 'status_ketersediaan')
        }),
        ('Detail & Harga', {
            'fields': ('deskripsi', 'harga_per_bulan')
        }),
    )

@admin.register(Penyewa)
class PenyewaAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'kamar_info', 'nomor_telepon', 'tanggal_mulai_sewa')
    search_fields = ('nama_lengkap', 'nomor_telepon')
    list_filter = ('tanggal_mulai_sewa',)
    autocomplete_fields = ['kamar'] # Membuat field kamar menjadi search-box

    def kamar_info(self, obj):
        if obj.kamar:
            return obj.kamar.nomor_kamar
        return "-"
    kamar_info.short_description = 'Menempati Kamar'

