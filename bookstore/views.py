from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import TheLoai, TacGia, DauSach, CT_TACGIA, Sach, PhieuNhapSach, CT_PNS, THAMSO, KhachHang, PhieuThuTien, HoaDon, CT_HD, BC_TON, BC_CONGNO
from .forms import TheLoaiForm, TacGiaForm, DauSachForm, CTTGForm, SachForm, PhieuNhapSachForm, CTPNSForm, KhachHangForm, PhieuThuTienForm, HoaDonForm, CTHDForm, ThamSoForm, BCTONForm, BCCNForm

# Mo trang thong tin nha sach
def bookstore(request):
    return render(request, 'bookstore/bookstore-info.html')

# Mo trang thong tin chi tiet cua 1 sach
def book(request, pk):
    return render(request, 'bookstore/single-book.html')

# Lap phieu nhap sach
def importBook(request):
    if request.method == 'POST':
        theloai_form = TheLoaiForm(request.POST, prefix = "theloai")
        tacgia_form = TacGiaForm(request.POST, prefix = "tacgia")
        dausach_form = DauSachForm(request.POST, prefix = "dausach")
        cttg_form = CTTGForm(request.POST, prefix = "cttg")
        sach_form = SachForm(request.POST, request.FILES, prefix = "sach")
        phieunhapsach_form = PhieuNhapSachForm(request.POST, prefix = "phieunhapsach")
        ctpns_form = CTPNSForm(request.POST, prefix = "ctpns")
        if theloai_form.is_valid() and tacgia_form.is_valid() and dausach_form.is_valid() and cttg_form.is_valid() and sach_form.is_valid() and phieunhapsach_form.is_valid() and ctpns_form.is_valid():
                     
            cttg = cttg_form.save(commit=False)
            theloai = theloai_form.save(commit=False)
            dausach = dausach_form.save(commit=False)
            tacgia = tacgia_form.save(commit=False)
            sach = sach_form.save(commit=False)
            phieunhapsach = phieunhapsach_form.save(commit=False)
            ctpns = ctpns_form.save(commit=False)

            if ctpns.so_luong_nhap < THAMSO.objects.all()[0].sl_nhap_toi_thieu:
                print("The number of books imported must be at least 150!")
                print("Import book failed!")
                return redirect('import-book')
            
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
            else:
                check_cttg = CT_TACGIA.objects.filter(ma_tac_gia=cttg.ma_tac_gia_id, ma_dau_sach=cttg.ma_dau_sach_id).exists()
                if check_cttg == False:
                    cttg.save()
            
            # Kiem tra ma sach da co trong table Sach hay chua?
            check_sach = Sach.objects.filter(ma_sach=ctpns.ma_sach_id).exists()
            if check_sach:
                sach = Sach.objects.get(ma_sach=ctpns.ma_sach_id)
            else:
                if sach.nha_xuat_ban != None and sach.nam_xuat_ban != None:
                    ma_dau_sach = DauSach.objects.get(ma_dau_sach=dausach.ma_dau_sach)
                    sach.ma_dau_sach = ma_dau_sach 
                    sach.save()
            
            if sach.so_luong_ton > THAMSO.objects.all()[0].sl_ton_toi_da:
                print("Only import books which are fewer than 300!")
                print("Import book failed!")
                return redirect('import-book')

            # Cap nhat tac gia cho sach
            sach = Sach.objects.get(ma_sach=sach.ma_sach, ma_dau_sach=dausach.ma_dau_sach)
            ds_tacgia = CT_TACGIA.objects.filter(ma_dau_sach=dausach.ma_dau_sach)
            tacgia_info = []
            for tacgia in ds_tacgia:
                tacgia_info.append(TacGia.objects.get(ma_tac_gia=tacgia.ma_tac_gia_id))
            
            tacgia_list = []
            for info in tacgia_info:
                tacgia_list.append(info.ten_tac_gia)
            
            sach.tac_gia = ", ".join(tacgia_list)
            sach.save()

            # Kiem tra ma phieu nhap da co trong table PhieuNhapSach hay chua?
            check_phieu_nhap_sach = PhieuNhapSach.objects.filter(ma_phieu_nhap=ctpns.ma_phieu_nhap_id).exists()
            if check_phieu_nhap_sach:
                phieunhapsach = PhieuNhapSach.objects.get(ma_phieu_nhap=ctpns.ma_phieu_nhap_id)
            else:
                phieunhapsach = phieunhapsach_form.save()
            
            # Kiem tra ma phieu nhap va ma sach da co trong table CT_PNS hay chua?
            check_ctpns = CT_PNS.objects.filter(ma_phieu_nhap=phieunhapsach.ma_phieu_nhap, ma_sach=sach.ma_sach).exists()
            if check_ctpns == False:
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
                print("Import book successfully!")
            
            return redirect('bookstore')
        else:
            print("Import book failed!")
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
    return render(request, 'bookstore/book-import-form.html', context)


# Lap phieu thu tien
def createReceipt(request):
    if request.method == 'POST':
        khachhang_form = KhachHangForm(request.POST, prefix = "khachhang")
        phieuthutien_form = PhieuThuTienForm(request.POST, prefix = "phieuthutien")
        if khachhang_form.is_valid() and phieuthutien_form.is_valid():

            khachhang = khachhang_form.save(commit=False)
            phieuthutien = phieuthutien_form.save(commit=False)

            # Kiem tra ma khach hang da co trong table KhachHang hay chua?
            check_khach_hang = KhachHang.objects.filter(ma_kh=phieuthutien.ma_kh_id).exists()
            if check_khach_hang:
                khachhang = KhachHang.objects.get(ma_kh=phieuthutien.ma_kh_id)
            else:
                if khachhang.hoten_kh != None:
                    khachhang = khachhang_form.save()

            phieuthutien = PhieuThuTien(
                ma_kh=khachhang,
                so_tien_thu=phieuthutien.so_tien_thu
            )
            kh = KhachHang.objects.get(ma_kh=khachhang.ma_kh)
            if THAMSO.objects.all()[0].kiem_tra_so_tien_thu == True:
                if phieuthutien.so_tien_thu <= kh.so_tien_no:
                    kh.so_tien_no -= phieuthutien.so_tien_thu
                    kh.save()
                    phieuthutien.save()
                    print("Create receipt successfully!")
                else:
                    print("The amount collected must not exceed the amount the customer owes!")
                    print("Create receipt failed!")
                    return redirect('create-receipt')
            else:
                kh.so_tien_no -= phieuthutien.so_tien_thu
                kh.save()
                phieuthutien.save()
                print("Create receipt successfully!")

            return redirect('bookstore')

        else:
            print("Create receipt failed!")

    else:
        khachhang_form = KhachHangForm(prefix = "khachhang")
        phieuthutien_form = PhieuThuTienForm(prefix = "phieuthutien")

    context = {
        'khachhang_form': khachhang_form,
        'phieuthutien_form': phieuthutien_form,
    }
    return render(request, 'bookstore/receipt-form.html', context)


# Tra cuu sach
def searchBooks(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    books = Sach.objects.filter(
        Q(ma_sach__icontains=search_query) | 
        Q(ma_dau_sach__ten_dau_sach__icontains=search_query) | 
        Q(ma_dau_sach__ma_the_loai__ten_the_loai__icontains=search_query) | 
        Q(nha_xuat_ban__icontains=search_query) | 
        Q(nam_xuat_ban__icontains=search_query) | 
        Q(so_luong_ton__icontains=search_query) | 
        Q(gia_tien__icontains=search_query) | 
        Q(tac_gia__icontains=search_query)
    )

    context = {'books': books, 'search_query': search_query}
    return render(request, 'bookstore/search-books.html', context)


# Tra cuu tac gia
def searchAuthors(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    authors = TacGia.objects.filter(
        Q(ma_tac_gia__icontains=search_query) | 
        Q(ten_tac_gia__icontains=search_query)
    )

    context = {'authors': authors, 'search_query': search_query}
    return render(request, 'bookstore/search-authors.html', context)


# Tra cuu khach hang
def searchGuests(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    guests = KhachHang.objects.filter(
        Q(ma_kh__icontains=search_query) | 
        Q(hoten_kh__icontains=search_query) | 
        Q(dia_chi__icontains=search_query) | 
        Q(dien_thoai__icontains=search_query) | 
        Q(email__icontains=search_query) | 
        Q(so_tien_no__icontains=search_query)
    )

    context = {'guests': guests, 'search_query': search_query}
    return render(request, 'bookstore/search-guests.html', context)


# Lap hoa don ban sach
def createBooksBill(request):
    if request.method == 'POST':
        khachhang_form = KhachHangForm(request.POST, prefix = "khachhang")
        hoadon_form = HoaDonForm(request.POST, prefix = "hoadon")
        cthd_form = CTHDForm(request.POST, prefix = "cthd")
        
        if khachhang_form.is_valid() and hoadon_form.is_valid() and cthd_form.is_valid():
            
            khachhang = khachhang_form.save(commit=False)
            hoadon = hoadon_form.save(commit=False)
            cthd = cthd_form.save(commit=False)
            
            # Kiem tra ma khach hang da co trong table KhachHang hay chua?
            check_khach_hang = KhachHang.objects.filter(ma_kh=hoadon.ma_kh_id).exists()
            if check_khach_hang:
                khachhang = KhachHang.objects.get(ma_kh=hoadon.ma_kh_id)
                if khachhang.so_tien_no > THAMSO.objects.all()[0].so_tien_no_toi_da:
                    print("This guest's debt is over 1000000 VND")
                    print("Create books bill failed!")
                    return redirect('create-books-bill')
            else:
                if khachhang.hoten_kh != None:
                    khachhang = khachhang_form.save()

            # Kiem tra ma hoa don da co trong table HoaDon hay chua?
            check_hoa_don = HoaDon.objects.filter(ma_hoa_don=cthd.ma_hoa_don_id).exists()
            if check_hoa_don:
                hoadon = HoaDon.objects.get(ma_hoa_don=cthd.ma_hoa_don_id)
            else:
                ma_kh = KhachHang.objects.get(ma_kh=khachhang.ma_kh)
                hoadon = HoaDon(
                    ma_kh=ma_kh
                )
                hoadon.save()

            # Kiem tra ma hoa don va ma sach da co trong table CT_HD hay chua?
            check_cthd = CT_HD.objects.filter(ma_hoa_don=hoadon.ma_hoa_don, ma_sach=cthd.ma_sach_id).exists()
            if check_cthd == False:
                ma_hoa_don = HoaDon.objects.get(ma_hoa_don=hoadon.ma_hoa_don)
                ma_sach = Sach.objects.get(ma_sach=cthd.ma_sach_id)
                cthd = CT_HD(
                    ma_hoa_don=ma_hoa_don,
                    ma_sach=ma_sach,
                    so_luong_ban=cthd.so_luong_ban,
                    don_gia_ban=ma_sach.gia_tien,
                    thanh_tien=cthd.so_luong_ban*ma_sach.gia_tien
                )
                
                sach = Sach.objects.get(ma_sach=cthd.ma_sach_id)
                ds_sach = Sach.objects.filter(ma_dau_sach=sach.ma_dau_sach)
                tong_sl_sach_cua_ds = 0
                for s in ds_sach:
                    tong_sl_sach_cua_ds += s.so_luong_ton

                tong_sl_sach_cua_ds -= cthd.so_luong_ban
                if tong_sl_sach_cua_ds < THAMSO.objects.all()[0].sl_ton_toi_thieu_sau_ban:
                    print("The number of books after selling must be at least 20!")
                    print("Create books bill failed!")
                    return redirect('create-books-bill')
                
                if (sach.so_luong_ton < cthd.so_luong_ban):
                    print("The number of books selling must not be bigger than the number of books stored")
                    print("Create books bill failed!")
                    return redirect('create-books-bill')

                sach.so_luong_ton -= cthd.so_luong_ban
                sach.save()
                cthd.save()
                hoadon = HoaDon.objects.get(ma_hoa_don=cthd.ma_hoa_don_id)
                hoadon.tong_tien += cthd.thanh_tien
                hoadon.save()
                print("Create books bill successfully!")

            return redirect('bookstore')
        else:
            print("Create books bill failed!")
    else:
        khachhang_form = KhachHangForm(prefix = "khachhang")
        hoadon_form = HoaDonForm(prefix = "hoadon")
        cthd_form = CTHDForm(prefix = "cthd")

    context = {
        'khachhang_form': khachhang_form,
        'hoadon_form': hoadon_form,
        'cthd_form': cthd_form,
    }
    return render(request, 'bookstore/books-bill-form.html', context)


# Nhap so tien tra
def inputPayment(request):
    if request.method == 'POST':
        hoadon_form = HoaDonForm(request.POST, prefix = "hoadon")
        cthd_form = CTHDForm(request.POST, prefix = "cthd")
        
        if hoadon_form.is_valid() and cthd_form.is_valid():
            
            hoadon = hoadon_form.save(commit=False)
            cthd = cthd_form.save(commit=False)
            
            # Kiem tra ma hoa don da nhap hay chua?
            check_hoa_don = HoaDon.objects.filter(ma_hoa_don=cthd.ma_hoa_don_id).exists()
            if check_hoa_don:
                hd = HoaDon.objects.get(ma_hoa_don=cthd.ma_hoa_don_id)
            else:
                print("Please input bill id")
                print("Input payment failed!")
                return redirect('input-payment')

            hd.so_tien_tra = hoadon.so_tien_tra
            # Kiem tra so tien tra
            if hd.so_tien_tra >= hd.tong_tien:
                hd.con_lai = hd.so_tien_tra - hd.tong_tien
                hd.save()
                print("Input payment successfully!")
            else:
                hd.con_lai = hd.so_tien_tra - hd.tong_tien
                hd.save()
                print("Input payment successfully!")
                kh = KhachHang.objects.get(ma_kh=hd.ma_kh_id)
                kh.so_tien_no -= hd.con_lai
                kh.save()
                print("The guest's debt has been updated!") 

            return redirect('bookstore')
        else:
            print("Input payment failed!")
    else:
        hoadon_form = HoaDonForm(prefix = "hoadon")
        cthd_form = CTHDForm(prefix = "cthd")

    context = {
        'hoadon_form': hoadon_form,
        'cthd_form': cthd_form,
    }
    return render(request, 'bookstore/input-payment.html', context)


# Tra cuu hoa don
def searchBills(request):
    search_query = 0

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    bill_detail = CT_HD.objects.filter(
        Q(ma_hoa_don__exact=search_query)
    )
    
    if search_query != 0 and HoaDon.objects.filter(ma_hoa_don=search_query).count() != 0:
        bill = HoaDon.objects.get(ma_hoa_don=search_query)
    else:
        bill = HoaDon.objects.filter(ma_hoa_don=search_query)

    context = {'bill_detail': bill_detail, 'bill': bill, 'search_query': search_query}
    return render(request, 'bookstore/search-bills.html', context)


# Tra cuu phieu nhap sach
def searchImportNotes(request):
    search_query = 0

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    note_detail = CT_PNS.objects.filter(
        Q(ma_phieu_nhap__exact=search_query)
    )
    
    if search_query != 0 and PhieuNhapSach.objects.filter(ma_phieu_nhap=search_query).count() != 0:
        note = PhieuNhapSach.objects.get(ma_phieu_nhap=search_query)
    else:
        note = PhieuNhapSach.objects.filter(ma_phieu_nhap=search_query)

    context = {'note_detail': note_detail, 'note': note, 'search_query': search_query}
    return render(request, 'bookstore/search-import-notes.html', context)


# Thay doi quy dinh
def changeRules(request):
    thamso = THAMSO.objects.all()[0]
    form = ThamSoForm(instance=thamso)

    if request.method == 'POST':
        form = ThamSoForm(request.POST, instance=thamso)
        if form.is_valid():
            form.save()
            return redirect('change-rules')

    context = {'form': form}
    return render(request, 'bookstore/change-rules.html', context)


# Lap bao cao ton
def createInventoryReport(request):
    if request.method == 'POST':
        bcton_form = BCTONForm(request.POST, prefix = "bcton")
        if bcton_form.is_valid():

            bcton = bcton_form.save(commit=False)

            # Kiem tra ma sach da nhap hay chua?
            check_sach = Sach.objects.filter(ma_sach=bcton.ma_sach_id).exists()
            if check_sach:
                sach = Sach.objects.get(ma_sach=bcton.ma_sach_id)
            else:
                print("Please input book id")
                print("Create inventory report failed!")
                return redirect('create-inventory-report')

            # Kiem tra thang da nhap hop le hay chua?
            if bcton.thang == None or bcton.thang < 1 or bcton.thang > 12:
                print("Please input a valid month")
                print("Create inventory report failed!")
                return redirect('create-inventory-report')

            # Kiem tra nam da nhap hop le hay chua?
            if bcton.nam == None or bcton.nam < 1:
                print("Please input a valid year")
                print("Create inventory report failed!")
                return redirect('create-inventory-report')

            # Kiem tra ma sach, thang, nam da co trong table BC_TON hay chua?
            check_bcton = BC_TON.objects.filter(ma_sach=bcton.ma_sach_id, thang=bcton.thang, nam=bcton.nam).exists()
            if check_bcton == False:

                ds_sach_nhap = CT_PNS.objects.filter(
                    ma_phieu_nhap__ngay_nhap__month=bcton.thang,
                    ma_phieu_nhap__ngay_nhap__year=bcton.nam,
                    ma_sach=bcton.ma_sach_id
                )

                for book in ds_sach_nhap:
                    bcton.phat_sinh += book.so_luong_nhap

                ds_sach_ban = CT_HD.objects.filter(
                    ma_hoa_don__ngay_lap__month=bcton.thang,
                    ma_hoa_don__ngay_lap__year=bcton.nam,
                    ma_sach=bcton.ma_sach_id
                )

                sl_sach_ban = 0
                for book in ds_sach_ban:
                    sl_sach_ban += book.so_luong_ban

                bcton.ton_cuoi = sach.so_luong_ton
                bcton.ton_dau = bcton.ton_cuoi - bcton.phat_sinh + sl_sach_ban

                bcton.save()
                print("Create inventory report successfully!")
            else:
                print("Already has!")
                print("Create inventory report failed!")
                return redirect('create-inventory-report')

            return redirect('bookstore')

        else:
            print("Create inventory report failed!")

    else:
        bcton_form = BCTONForm(prefix = "bcton")

    context = {
        'bcton_form': bcton_form,
    }
    return render(request, 'bookstore/create-inventory-report.html', context)


# Tra cuu bao cao ton
def searchInventoryReport(request):
    search_month = 0
    search_year = 0

    if request.GET.get('search_month'):
        search_month = request.GET.get('search_month')
    if request.GET.get('search_year'):
        search_year = request.GET.get('search_year')
    
    report = BC_TON.objects.filter(
        Q(thang__exact=search_month),
        Q(nam__exact=search_year)
    )

    context = {'report': report, 'search_month': search_month, 'search_year': search_year}
    return render(request, 'bookstore/search-inventory-report.html', context)


# Lap bao cao cong no
def createDebtReport(request):
    if request.method == 'POST':
        bccn_form = BCCNForm(request.POST, prefix = "bccn")
        if bccn_form.is_valid():

            bccn = bccn_form.save(commit=False)

            # Kiem tra ma khach hang da nhap hay chua?
            check_khach_hang = KhachHang.objects.filter(ma_kh=bccn.ma_kh_id).exists()
            if check_khach_hang:
                khachhang = KhachHang.objects.get(ma_kh=bccn.ma_kh_id)
            else:
                print("Please input guest id")
                print("Create debt report failed!")
                return redirect('create-debt-report')

            # Kiem tra thang da nhap hop le hay chua?
            if bccn.thang == None or bccn.thang < 1 or bccn.thang > 12:
                print("Please input a valid month")
                print("Create debt report failed!")
                return redirect('create-debt-report')

            # Kiem tra nam da nhap hop le hay chua?
            if bccn.nam == None or bccn.nam < 1:
                print("Please input a valid year")
                print("Create debt report failed!")
                return redirect('create-debt-report')
            
            # Kiem tra ma khach hang, thang, nam da co trong table BC_CONGNO hay chua?
            check_bccn = BC_CONGNO.objects.filter(ma_kh=bccn.ma_kh_id, thang=bccn.thang, nam=bccn.nam).exists()
            if check_bccn == False:

                ds_kh_no = HoaDon.objects.filter(
                    ngay_lap__month=bccn.thang,
                    ngay_lap__year=bccn.nam,
                    ma_kh=bccn.ma_kh_id
                )

                for guest in ds_kh_no:
                    bccn.phat_sinh -= guest.con_lai

                ds_kh_tra_no = PhieuThuTien.objects.filter(
                    ngay_thu_tien__month=bccn.thang,
                    ngay_thu_tien__year=bccn.nam,
                    ma_kh=bccn.ma_kh_id
                )

                tong_so_tien_kh_tra_no = 0
                for guest in ds_kh_tra_no:
                    tong_so_tien_kh_tra_no += guest.so_tien_thu

                bccn.no_cuoi = khachhang.so_tien_no
                bccn.no_dau = bccn.no_cuoi - bccn.phat_sinh + tong_so_tien_kh_tra_no
            
                bccn.save()
                print("Create debt report successfully!")
            else:
                print("Already has!")
                print("Create debt report failed!")
                return redirect('create-debt-report')
            
            return redirect('bookstore')

        else:
            print("Create debt report failed!")

    else:
        bccn_form = BCCNForm(prefix = "bccn")

    context = {
        'bccn_form': bccn_form,
    }
    return render(request, 'bookstore/create-debt-report.html', context)


# Tra cuu bao cao cong no
def searchDebtReport(request):
    search_month = 0
    search_year = 0

    if request.GET.get('search_month'):
        search_month = request.GET.get('search_month')
    if request.GET.get('search_year'):
        search_year = request.GET.get('search_year')
    
    report = BC_CONGNO.objects.filter(
        Q(thang__exact=search_month),
        Q(nam__exact=search_year)
    )

    context = {'report': report, 'search_month': search_month, 'search_year': search_year}
    return render(request, 'bookstore/search-debt-report.html', context)