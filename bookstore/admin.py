from django.contrib import admin

# Register your models here.
from .models import TheLoai, DauSach, Sach, KhachHang, PhieuThuTien, HoaDon, CT_HD, PhieuNhapSach, CT_PNS, BC_TON, BC_CONGNO

my_models = [TheLoai, DauSach, Sach, KhachHang, PhieuThuTien, HoaDon, CT_HD, PhieuNhapSach, CT_PNS, BC_TON, BC_CONGNO]
admin.site.register(my_models)
