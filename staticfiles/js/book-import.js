document.addEventListener('DOMContentLoaded', function() {
    var ma_dau_sach = document.getElementById("id_cttg-ma_dau_sach");
    var ten_dau_sach = document.getElementById("id_dausach-ten_dau_sach");

    ma_dau_sach.addEventListener('input', function() {
        ten_dau_sach.disabled = ma_dau_sach.value.trim();
        ten_dau_sach.value = null;
    });

    var ma_the_loai = document.getElementById("id_dausach-ma_the_loai");
    var ten_the_loai = document.getElementById("id_theloai-ten_the_loai");

    ma_the_loai.addEventListener('input', function() {
        ten_the_loai.disabled = ma_the_loai.value.trim();
        ten_the_loai.value = null;
    });

    var ma_tac_gia = document.getElementById("id_cttg-ma_tac_gia");
    var ten_tac_gia = document.getElementById("id_tacgia-ten_tac_gia");

    ma_tac_gia.addEventListener('input', function() {
        ten_tac_gia.disabled = ma_tac_gia.value.trim();
        ten_tac_gia.value = null;
    });

    var ma_sach = document.getElementById("id_ctpns-ma_sach");
    var nha_xuat_ban = document.getElementById("id_sach-nha_xuat_ban");
    var nam_xuat_ban = document.getElementById("id_sach-nam_xuat_ban");

    ma_sach.addEventListener('input', function() {
        nha_xuat_ban.disabled = ma_sach.value.trim();
        nam_xuat_ban.disabled = nha_xuat_ban.disabled;
        nha_xuat_ban.value = null;
        nam_xuat_ban.value = null;
    });
});