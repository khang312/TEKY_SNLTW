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
        self.perimeter = (self.legnth + self.width) * 2
        print(self.area, self.perimeter)
    


    pass

hinhChuNhat = HinhChuNhat()

hinhChuNhat.nhap_chieu_dai()
hinhChuNhat.nhap_chu_vi_va_dien_tich()