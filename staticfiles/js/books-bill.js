document.addEventListener('DOMContentLoaded', function() {
    var ma_kh = document.getElementById("id_hoadon-ma_kh");
    var hoten_kh = document.getElementById("id_khachhang-hoten_kh");

    ma_kh.addEventListener('input', function() {
        hoten_kh.disabled = ma_kh.value.trim();
        hoten_kh.value = null;
    });

    var ma_hoa_don = document.getElementById("id_cthd-ma_hoa_don");

    ma_hoa_don.addEventListener('input', function() {
        ma_kh.disabled = ma_hoa_don.value.trim();
        hoten_kh.disabled = ma_kh.disabled;
        ma_kh.value = null;
        hoten_kh.value = null;
    });
});