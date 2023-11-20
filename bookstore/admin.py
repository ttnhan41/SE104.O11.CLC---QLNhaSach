from django.contrib import admin

# Register your models here.
from .models import TheLoai, TacGia, DauSach, CT_TACGIA, Sach, KhachHang, PhieuThuTien, HoaDon, CT_HD, PhieuNhapSach, CT_PNS, BC_TON, BC_CONGNO, THAMSO

my_models = [TheLoai, TacGia, DauSach, CT_TACGIA, Sach, KhachHang, PhieuThuTien, HoaDon, CT_HD, PhieuNhapSach, CT_PNS, BC_TON, BC_CONGNO, THAMSO]
admin.site.register(my_models)
