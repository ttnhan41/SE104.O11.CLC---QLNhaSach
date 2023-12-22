document.addEventListener('DOMContentLoaded', function() {
    var ma_kh = document.getElementById("id_hoadon-ma_kh");
    var hoten_kh = document.getElementById("id_khachhang-hoten_kh");

    ma_kh.addEventListener('input', function() {
        hoten_kh.disabled = ma_kh.value.trim();
        hoten_kh.value = null;
    });
});