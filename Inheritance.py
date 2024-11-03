# Inheritance
class kereta:
    def __init__(self,nama,umur,alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def indentitas(self):
        return f"Nama : {self.nama}, Umur : {self.umur}, Alamat : {self.alamat}"
    
class kereta_eksekutif(kereta):
    def __init__(self, nama, umur, alamat, biaya, diskon):
        super().__init__(nama, umur, alamat)
        self.biaya = biaya
        self.diskon = diskon
 
    def biayaperjalanan(self):
        jumlah_biaya = self.biaya - self.diskon
        return f"Jumlah pembayaran {self.biaya} - Jumlah diskon {self.diskon} = {jumlah_biaya}"
    
    def tujuan(self):
        return f"Tujuan dari penumpang ini yaitu {self.alamat}"
    
    def infomakanan(self):
        return f"Makanan yang tersedia yaitu :\n1. Nasi Ayam Bakar\n2. Nasi Goreng\n3. Puding Caviar"
    
class kereta_ekonomis(kereta):
    def __init__(self, nama, umur, alamat, biaya, diskon):
        super().__init__(nama, umur, alamat)
        self.biaya = biaya
        self.diskon = diskon

    def biayaperjalanan(self):
        jumlah_biaya = self.biaya - self.diskon
        return f"Jumlah pembayaran {self.biaya} - Jumlah diskon {self.diskon} = {jumlah_biaya}"
    
    def tujuan(self):
        return f"Tujuan dari penumpang ini yaitu {self.alamat}"

kereta_a=kereta_eksekutif("Puja",19,"Palu",500.000,150.000)
kereta_b=kereta_ekonomis("Puji",17,"Makassar",250.000,50.000)

print(kereta_a.biayaperjalanan)
print(kereta_b.tujuan)
