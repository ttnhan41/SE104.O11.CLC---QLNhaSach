from django.db import models


class TheLoai(models.Model):
    ma_the_loai = models.AutoField(auto_created=True, primary_key=True)
    ten_the_loai = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.ma_the_loai)

class TacGia(models.Model):
    ma_tac_gia = models.AutoField(auto_created=True, primary_key=True)
    ten_tac_gia = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return str(self.ma_tac_gia)

class DauSach(models.Model):
    ma_dau_sach = models.AutoField(auto_created=True, primary_key=True)
    ten_dau_sach = models.CharField(max_length=50, null=True, blank=True)
    ma_the_loai = models.ForeignKey(TheLoai, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.ma_dau_sach)

class CT_TACGIA(models.Model):
    ma_dau_sach = models.ForeignKey(DauSach, on_delete=models.CASCADE, null=True, blank=True)
    ma_tac_gia = models.ForeignKey(TacGia, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Sach(models.Model):
    ma_sach = models.AutoField(auto_created=True, primary_key=True)
    ma_dau_sach = models.ForeignKey(DauSach, on_delete=models.CASCADE, null=True, blank=True)
    nha_xuat_ban = models.CharField(max_length=50, null=True, blank=True)
    nam_xuat_ban = models.IntegerField(null=True, blank=True)
    so_luong_ton = models.IntegerField(null=True, blank=True, default=0)
    gia_tien = models.FloatField(null=True, blank=True, default=0)
    tac_gia = models.TextField(null=True, blank=True) # Tao field nay de tra cuu sach theo tac gia

    def __str__(self):
        return str(self.ma_sach)

class KhachHang(models.Model):
    ma_kh = models.AutoField(auto_created=True, primary_key=True)
    hoten_kh = models.CharField(max_length=30, null=True, blank=True)
    dia_chi = models.CharField(max_length=50, null=True, blank=True)
    dien_thoai = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    so_tien_no = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.ma_kh)

class PhieuThuTien(models.Model):
    ma_phieu_thu = models.AutoField(auto_created=True, primary_key=True)
    ma_kh = models.ForeignKey(KhachHang, on_delete=models.CASCADE, null=True, blank=True)
    ngay_thu_tien = models.DateField(auto_now_add=True, blank=True)
    so_tien_thu = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.ma_phieu_thu)

class HoaDon(models.Model):
    ma_hoa_don = models.AutoField(auto_created=True, primary_key=True)
    ma_kh = models.ForeignKey(KhachHang, on_delete=models.CASCADE, null=True, blank=True)
    ngay_lap = models.DateField(auto_now_add=True, blank=True)
    tong_tien = models.FloatField(null=True, blank=True, default=0)
    so_tien_tra = models.FloatField(null=True, blank=True, default=0)
    con_lai = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.ma_hoa_don)

class CT_HD(models.Model):
    mact_hd = models.AutoField(auto_created=True, primary_key=True)
    ma_hoa_don = models.ForeignKey(HoaDon, on_delete=models.CASCADE, null=True, blank=True)
    ma_sach = models.ForeignKey(Sach, on_delete=models.CASCADE, null=True, blank=True)
    so_luong_ban = models.IntegerField(null=True, blank=True, default=0)
    don_gia_ban = models.FloatField(null=True, blank=True, default=0)
    thanh_tien = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.mact_hd)

class PhieuNhapSach(models.Model):
    ma_phieu_nhap = models.AutoField(auto_created=True, primary_key=True)
    ngay_nhap = models.DateField(auto_now_add=True, blank=True)
    tong_tien = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.ma_phieu_nhap)

class CT_PNS(models.Model):
    mact_pns = models.AutoField(auto_created=True, primary_key=True)
    ma_phieu_nhap = models.ForeignKey(PhieuNhapSach, on_delete=models.CASCADE, null=True, blank=True)
    ma_sach = models.ForeignKey(Sach, on_delete=models.CASCADE, null=True, blank=True)
    so_luong_nhap = models.IntegerField(null=True, blank=True, default=0)
    don_gia_nhap = models.FloatField(null=True, blank=True, default=0)
    thanh_tien = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.mact_pns)

class BC_TON(models.Model):
    mabc_ton = models.AutoField(auto_created=True, primary_key=True)
    ma_sach = models.ForeignKey(Sach, on_delete=models.CASCADE, null=True, blank=True)
    thang = models.IntegerField(null=True, blank=True)
    nam = models.IntegerField(null=True, blank=True)
    ton_dau = models.IntegerField(null=True, blank=True, default=0)
    phat_sinh = models.IntegerField(null=True, blank=True, default=0)
    ton_cuoi = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.mabc_ton)

class BC_CONGNO(models.Model):
    mabc_cn = models.AutoField(auto_created=True, primary_key=True)
    ma_kh = models.ForeignKey(KhachHang, on_delete=models.CASCADE, null=True, blank=True)
    thang = models.IntegerField(null=True, blank=True)
    nam = models.IntegerField(null=True, blank=True)
    no_dau = models.FloatField(null=True, blank=True, default=0)
    phat_sinh = models.FloatField(null=True, blank=True, default=0)
    no_cuoi = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.mabc_cn)

class THAMSO(models.Model):
    sl_nhap_toi_thieu = models.IntegerField(null=True, blank=True, default=150)
    sl_ton_toi_da = models.IntegerField(null=True, blank=True, default=299)
    so_tien_no_toi_da = models.FloatField(null=True, blank=True, default=1000000)
    sl_ton_toi_thieu_sau_ban = models.IntegerField(null=True, blank=True, default=20)
    ti_le_tinh_don_gia_ban = models.FloatField(null=True, blank=True, default=1.05)
    kiem_tra_so_tien_thu = models.BooleanField(default=True)

    def __str__(self):
        return 'TS'