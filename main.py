class HinhChuNhat:
    length = 0
    width = 0
    name = 'rectangle'
    area = 0
    perimeter = 0
    def nhap_chieu_dai_rong(self):
        self.length = int(input('nhap chieu dai'))
        self.width = int(input('nhap chieu rong'))   
    def tinh_chu_vi_va_dien_tich(self):
        self.area = self.length * self.width
        self.perimeter = (self.length + self.width) * 2
        print("area = ", self.area, "perimeter = ", self.perimeter)
    
    def kiem_tra_rectangle(self):
        if self.length == self.width:
            print('hinh nay la hinh vuong')
        else:
            print('ok hinh chu nhat')


    pass

hinhChuNhat = HinhChuNhat()

hinhChuNhat.nhap_chieu_dai_rong()
hinhChuNhat.tinh_chu_vi_va_dien_tich()
hinhChuNhat.kiem_tra_rectangle()