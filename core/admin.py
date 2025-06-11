from django.contrib import admin
from .models import Kamar, Penyewa

@admin.register(Kamar)
class KamarAdmin(admin.ModelAdmin):
    # Menambahkan 'foto_kamar' agar tampil di halaman daftar
    list_display = ('nomor_kamar', 'lantai', 'harga_per_bulan', 'status_ketersediaan', 'updated_at')
    list_filter = ('status_ketersediaan', 'lantai')
    search_fields = ('nomor_kamar',)
    ordering = ('nomor_kamar',)
    list_editable = ('harga_per_bulan', 'status_ketersediaan')
    
    # PERUBAHAN DI SINI:
    # Menambahkan field 'foto_kamar' ke dalam tampilan form edit/tambah
    fieldsets = (
        (None, {
            'fields': ('nomor_kamar', 'lantai', 'status_ketersediaan')
        }),
        ('Detail & Harga', {
            'fields': ('foto_kamar', 'deskripsi', 'harga_per_bulan')
        }),
    )

@admin.register(Penyewa)
class PenyewaAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'kamar_info', 'nomor_telepon', 'tanggal_mulai_sewa')
    search_fields = ('nama_lengkap', 'nomor_telepon')
    list_filter = ('tanggal_mulai_sewa',)
    autocomplete_fields = ['kamar']

    def kamar_info(self, obj):
        if obj.kamar:
            return obj.kamar.nomor_kamar
        return "-"
    kamar_info.short_description = 'Menempati Kamar'
