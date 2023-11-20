from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TheLoai, TacGia, DauSach, CT_TACGIA, Sach, PhieuNhapSach, CT_PNS, THAMSO
from .forms import TheLoaiForm, TacGiaForm, DauSachForm, CTTGForm, SachForm, PhieuNhapSachForm, CTPNSForm

# Create your views here.

# Trang thong tin cua tat ca sach
def books(request):
    return render(request, 'books/books.html')

# Trang thong tin chi tiet cua 1 sach
def book(request, pk):
    return render(request, 'books/single-book.html')

# Lap phieu nhap sach
def importBook(request):

    if request.method == 'POST':
        theloai_form = TheLoaiForm(request.POST, prefix = "theloai")
        tacgia_form = TacGiaForm(request.POST, prefix = "tacgia")
        dausach_form = DauSachForm(request.POST, prefix = "dausach")
        cttg_form = CTTGForm(request.POST, prefix = "cttg")
        sach_form = SachForm(request.POST, prefix = "sach")
        phieunhapsach_form = PhieuNhapSachForm(request.POST, prefix = "phieunhapsach")
        ctpns_form = CTPNSForm(request.POST, prefix = "ctpns")
        if theloai_form.is_valid() and tacgia_form.is_valid() and dausach_form.is_valid() and cttg_form.is_valid() and sach_form.is_valid() and phieunhapsach_form.is_valid() and ctpns_form.is_valid():
            print("Import successfully!")
            
            cttg = cttg_form.save(commit=False)
            theloai = theloai_form.save(commit=False)
            dausach = dausach_form.save(commit=False)
            tacgia = tacgia_form.save(commit=False)
            sach = sach_form.save(commit=False)
            phieunhapsach = phieunhapsach_form.save(commit=False)
            ctpns = ctpns_form.save(commit=False)
            
            # Kiem tra ma the loai da co trong table TheLoai hay chua?
            check_the_loai = TheLoai.objects.filter(ma_the_loai=dausach.ma_the_loai_id).exists()
            if check_the_loai:
                theloai = TheLoai.objects.get(ma_the_loai=dausach.ma_the_loai_id)
            else:
                if theloai.ten_the_loai != None:
                    theloai = theloai_form.save()
            
            # Kiem tra ma dau sach da co trong table DauSach hay chua?
            check_dau_sach = DauSach.objects.filter(ma_dau_sach=cttg.ma_dau_sach_id).exists()
            if check_dau_sach:
                dausach = DauSach.objects.get(ma_dau_sach=cttg.ma_dau_sach_id)
            else:
                if dausach.ten_dau_sach != None:
                    ma_the_loai = TheLoai.objects.get(ma_the_loai=theloai.ma_the_loai)
                    dausach = DauSach(
                        ten_dau_sach=dausach.ten_dau_sach,
                        ma_the_loai=ma_the_loai
                    )
                    dausach.save()
            
            # Kiem tra ma tac gia da co trong table TacGia hay chua?
            check_tac_gia = TacGia.objects.filter(ma_tac_gia=cttg.ma_tac_gia_id).exists()
            if check_tac_gia:
                tacgia = TacGia.objects.get(ma_tac_gia=cttg.ma_tac_gia_id)
            else:
                if tacgia.ten_tac_gia != None:
                    tacgia = tacgia_form.save()
            
            # Kiem tra ma tac gia va ma dau sach da co trong table CT_TACGIA hay chua?
            check_tac_gia = CT_TACGIA.objects.filter(ma_tac_gia=tacgia.ma_tac_gia).exists()
            check_dau_sach = CT_TACGIA.objects.filter(ma_dau_sach=dausach.ma_dau_sach).exists()
            if check_tac_gia == False or check_dau_sach == False:
                ma_tac_gia = TacGia.objects.get(ma_tac_gia=tacgia.ma_tac_gia)
                ma_dau_sach = DauSach.objects.get(ma_dau_sach=dausach.ma_dau_sach)
                cttg = CT_TACGIA(
                    ma_dau_sach=ma_dau_sach,
                    ma_tac_gia=ma_tac_gia
                )
                cttg.save()
            
            # Kiem tra ma sach da co trong table Sach hay chua?
            check_sach = Sach.objects.filter(ma_sach=ctpns.ma_sach_id).exists()
            if check_sach:
                sach = Sach.objects.get(ma_sach=ctpns.ma_sach_id)
            else:
                if sach.nha_xuat_ban != None and sach.nam_xuat_ban != None:
                    ma_dau_sach = DauSach.objects.get(ma_dau_sach=dausach.ma_dau_sach)
                    sach = Sach(
                        ma_dau_sach=ma_dau_sach,
                        nha_xuat_ban=sach.nha_xuat_ban,
                        nam_xuat_ban=sach.nam_xuat_ban
                    )
                    sach.save()
            
            # Kiem tra ma phieu nhap da co trong table PhieuNhapSach hay chua?
            check_phieu_nhap_sach = PhieuNhapSach.objects.filter(ma_phieu_nhap=ctpns.ma_phieu_nhap_id).exists()
            if check_phieu_nhap_sach:
                phieunhapsach = PhieuNhapSach.objects.get(ma_phieu_nhap=ctpns.ma_phieu_nhap_id)
            else:
                phieunhapsach = phieunhapsach_form.save()
            
            # Kiem tra ma phieu nhap va ma sach da co trong table CT_PNS hay chua?
            check_phieu_nhap_sach = CT_PNS.objects.filter(ma_phieu_nhap=phieunhapsach.ma_phieu_nhap).exists()
            check_sach = CT_PNS.objects.filter(ma_sach=sach.ma_sach).exists()
            if check_phieu_nhap_sach == False or check_sach == False:
                ma_phieu_nhap = PhieuNhapSach.objects.get(ma_phieu_nhap=phieunhapsach.ma_phieu_nhap)
                ma_sach = Sach.objects.get(ma_sach=sach.ma_sach)
                ctpns = CT_PNS(
                    ma_phieu_nhap=ma_phieu_nhap,
                    ma_sach=ma_sach,
                    so_luong_nhap=ctpns.so_luong_nhap,
                    don_gia_nhap=ctpns.don_gia_nhap,
                    thanh_tien=ctpns.so_luong_nhap*ctpns.don_gia_nhap
                )
                ctpns.save()
                sach = Sach.objects.get(ma_sach=ctpns.ma_sach_id)
                sach.so_luong_ton += ctpns.so_luong_nhap
                sach.gia_tien = THAMSO.objects.all()[0].ti_le_tinh_don_gia_ban * ctpns.don_gia_nhap
                sach.save()
                phieunhapsach = PhieuNhapSach.objects.get(ma_phieu_nhap=ctpns.ma_phieu_nhap_id)
                phieunhapsach.tong_tien += ctpns.thanh_tien
                phieunhapsach.save()
                
            return redirect('books')
        else:
            print("Import failed!")
    else:
        theloai_form = TheLoaiForm(prefix = "theloai")
        tacgia_form = TacGiaForm(prefix = "tacgia")
        dausach_form = DauSachForm(prefix = "dausach")
        cttg_form = CTTGForm(prefix = "cttg")
        sach_form = SachForm(prefix = "sach")
        phieunhapsach_form = PhieuNhapSachForm(prefix = "phieunhapsach")
        ctpns_form = CTPNSForm(prefix = "ctpns")

    context = {
        'theloai_form': theloai_form,
        'tacgia_form': tacgia_form,
        'dausach_form': dausach_form,
        'cttg_form': cttg_form,
        'sach_form': sach_form,
        'phieunhapsach_form': phieunhapsach_form,
        'ctpns_form': ctpns_form,
    }
    return render(request, 'books/book-import-form.html', context)
