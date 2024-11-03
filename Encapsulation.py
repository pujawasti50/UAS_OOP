# Encapsulation
class biodata():
    def __init__(self):
        self.mahasiswa = "Mahasiswa UIN"

    def lihat_kampus(self):
        return self.mahasiswa
    
    def ubah_kampus(self,kampus):
        self.mahasiswa = kampus
    
    def kelas(self):
        return "Anda berada di kelas A"
    
    def lihatkelas(self):
        return self.kelas()

    def semuanya(self):
        print("Fungsi ini untuk melihat semua data")
        print(self.mahasiswa)
        print(self.kelas)

class formulir(biodata):
    def __init__(self):
        super().__init__()

    def demoturunan(self):

        biodata = self.lihat_kampus()
        print(f"Ini adalah biodata yang ada {biodata}")

        self.ubah_kampus("Mahasiswa UGM")
        kampus_baru = self.lihat_kampus()
        print(f"Kampus yang berhasil diubah yaitu {kampus_baru}")

        kelas = self.lihatkelas()
        print(f"Sekarang {kelas}")

objekturunan = formulir()
objekturunan.demoturunan()