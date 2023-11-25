from django.forms import ModelForm
from .models import TheLoai, TacGia, DauSach, CT_TACGIA, Sach, PhieuNhapSach, CT_PNS, KhachHang, PhieuThuTien

class TheLoaiForm(ModelForm):
    class Meta:
        model = TheLoai
        fields = ['ten_the_loai']

class TacGiaForm(ModelForm):
    class Meta:
        model = TacGia
        fields = ['ten_tac_gia']

class DauSachForm(ModelForm):
    class Meta:
        model = DauSach
        fields = ['ten_dau_sach', 'ma_the_loai']

class CTTGForm(ModelForm):
    class Meta:
        model = CT_TACGIA
        fields = '__all__'

class SachForm(ModelForm):
    class Meta:
        model = Sach
        fields = ['ma_dau_sach', 'nha_xuat_ban', 'nam_xuat_ban']
        

class PhieuNhapSachForm(ModelForm):
    class Meta:
        model = PhieuNhapSach
        fields = '__all__'


class CTPNSForm(ModelForm):
    class Meta:
        model = CT_PNS
        fields = ['ma_phieu_nhap', 'ma_sach', 'so_luong_nhap', 'don_gia_nhap']


class KhachHangForm(ModelForm):
    class Meta:
        model = KhachHang
        fields = ['hoten_kh', 'dia_chi', 'dien_thoai', 'email']


class PhieuThuTienForm(ModelForm):
    class Meta:
        model = PhieuThuTien
        fields = ['ma_kh', 'so_tien_thu']
        
