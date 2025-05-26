from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if (self.soluongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id 
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def soluongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svid = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))
        sv = SinhVien(svid, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = SinhVien.self.findByID(ID) 
        if (sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = int(input("Nhập chuyên ngành của sinh viên: ")) 
            diemTB = float(input("Nhập điểm của sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByMajor(self):
        self.listSinhVien.sort(key=lambda x: x._major, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        searchResult = None
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv: SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung binh"
        else 
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8}{:<18}{:<8}{:<8}{:<8}{:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if (len(listSV) > 0): # Dùng len() thay cho __len__()
            for sv in listSV:
                print("{:<8}{:<18}{:<8}{:<8}{:<8}{:<8}".format(
                    sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))

        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien    
