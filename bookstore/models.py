from django.db import models
import uuid
# Create your models here.

class TheLoai(models.Model):
    ma_the_loai = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ten_the_loai = models.CharField(max_length=50, null=False, blank=False)

class DauSach(models.Model):
    ma_dau_sach = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ten_dau_sach = models.CharField(max_length=50, null=False, blank=False)
    ma_the_loai = models.ForeignKey(TheLoai, on_delete=models.SET_NULL, null=True)
    tac_gia = models.CharField(max_length=30, null=False, blank=False)

class Sach(models.Model):
    ma_sach = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ma_dau_sach = models.ForeignKey(DauSach, on_delete=models.CASCADE)
    nha_xuat_ban = models.CharField(max_length=50, null=False, blank=False)
    nam_xuat_ban = models.IntegerField(null=False, blank=False)
    so_luong_ton = models.IntegerField(null=False, blank=False)
    gia_tien = models.FloatField(null=False, blank=False)

class KhachHang(models.Model):
    ma_kh = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    hoten_kh = models.CharField(max_length=30, null=False, blank=False)
    dia_chi = models.CharField(max_length=50, null=False, blank=False)
    dien_thoai = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    so_tien_no = models.FloatField(null=False, blank=False)

class PhieuThuTien(models.Model):
    ma_phieu_thu = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ma_kh = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    ngay_thu_tien = models.DateField(auto_now_add=True, blank=True)
    so_tien_thu = models.FloatField(null=False, blank=False)

class HoaDon(models.Model):
    ma_hoa_don = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ma_kh = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    ngay_lap = models.DateField(auto_now_add=True, blank=True)
    tong_tien = models.FloatField(null=False, blank=True)
    so_tien_tra = models.FloatField(null=False, blank=False)

class CT_HD(models.Model):
    mact_hd = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ma_hoa_don = models.ForeignKey(HoaDon, on_delete=models.CASCADE)
    ma_sach = models.ForeignKey(Sach, on_delete=models.CASCADE)
    so_luong_ban = models.IntegerField(null=False, blank=False)
    don_gia_ban = models.FloatField(null=False, blank=False)
    thanh_tien = models.FloatField(null=False, blank=True)

class PhieuNhapSach(models.Model):
    ma_phieu_nhap = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ngay_nhap = models.DateField(auto_now_add=True, blank=True)
    tong_tien = models.FloatField(null=False, blank=True)

class CT_PNS(models.Model):
    mact_pns = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ma_phieu_nhap = models.ForeignKey(PhieuNhapSach, on_delete=models.CASCADE)
    ma_sach = models.ForeignKey(Sach, on_delete=models.CASCADE)
    so_luong_nhap = models.IntegerField(null=False, blank=False)
    don_gia_nhap = models.FloatField(null=False, blank=False)
    thanh_tien = models.FloatField(null=False, blank=True)

class BC_TON(models.Model):
    mabc_ton = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ma_sach = models.ForeignKey(Sach, on_delete=models.CASCADE)
    thang = models.IntegerField(null=False, blank=False)
    nam = models.IntegerField(null=False, blank=False)
    ton_dau = models.IntegerField(null=False, blank=False)
    phat_sinh = models.IntegerField(null=False, blank=False)
    ton_cuoi = models.IntegerField(null=False, blank=False)

class BC_CONGNO(models.Model):
    mabc_cn = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ma_kh = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    thang = models.IntegerField(null=False, blank=False)
    nam = models.IntegerField(null=False, blank=False)
    no_dau = models.FloatField(null=False, blank=False)
    phat_sinh = models.FloatField(null=False, blank=False)
    no_cuoi = models.FloatField(null=False, blank=False)


