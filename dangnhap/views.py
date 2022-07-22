from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from dangky.models import NguoiDung

# Create your views here.
def dangnhap(request):
    return render(request, 'dangnhap.html')

def xuly_dangnhap(request):
    ten = request.GET.get('ten')
    matkhau = request.GET.get('matkhau')

    thongtin = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau = matkhau)
    danh_sach = NguoiDung.objects.all()
    context = {
        'ds_nguoidung':danh_sach
    }
    if(thongtin.exists()):
        #return render(request, 'themnhanvien.html')
        return render(request, 'danhsach.html', context)
    else:
        return render(request, 'loi.html')

def chi_tiet(request, nguoidung_id):
    #print(nguoidung_id)
    nv = get_object_or_404(NguoiDung, pk = nguoidung_id)
    context = {
        'nguoi_dung':nv
    }

    return render(request, 'chitiet.html', context)

def xuly_capnhat(request):
    ten = request.GET.get('ten')
    matkhau = request.GET.get('matkhau')
    email = request.GET.get('mail')
    id_nguoidung = request.GET.get('id_nd')

    NguoiDung.objects.filter(id = id_nguoidung).update(
        ten_dang_nhap = ten,
        mat_khau = matkhau,
        email = email
    )

    
    danh_sach = NguoiDung.objects.all()
    context = {
        'ds_nguoidung':danh_sach
    }
    
        #return render(request, 'themnhanvien.html')
    return render(request, 'danhsach.html', context)

def xoa_nguoidung(request, nguoidung_id):
    dulieu = get_object_or_404(NguoiDung, pk = nguoidung_id)
    try:
        dulieu.delete()
    except:
        print("Xóa bị lỗi")


    danh_sach = NguoiDung.objects.all()
    context = {
        'ds_nguoidung':danh_sach
    }
    
    return render(request, 'danhsach.html', context)



  



    