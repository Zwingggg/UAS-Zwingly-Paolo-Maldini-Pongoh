import time

class Nasabah:
    def __init__(self, nama, prioritas=False):
        self.nama = nama
        self.prioritas = prioritas
        self.waktu_masuk = time.time() #waktu pada saat nasabah masuk pada antrian

class Loket:
    def __init__(self, id_loket):
        self.id_loket = id_loket
        self.nasabah_dilayani = None
        self.waktu_mulai = None

from collections import deque
from random import randint

class AntrianPelayanan:
    def __init__(self):
        self.antrian_biasa = deque() #Antrian untuk nasabah biasa
        self.antrian_prioritas = deque() #Antrian untuk nasabah prioritas
        self.lokets = []
        self.statistik = {'total_nasabah': 0, 'total_waktu': 0}
        self.loket_index = 0 #Index yang melacak loket yang akan melayani nasabah

    def tambah_nasabah(self, nama, prioritas=False):
        nasabah = Nasabah(nama, prioritas)
        if prioritas:
            self.antrian_prioritas.append(nasabah)
            print(f"Nasabah '{nama}' (Prioritas) Telah ditambahkan ke antrian")
        else:
            self.antrian_biasa.append(nasabah)
            print(f"Nasabah '{nama}' Telah ditambahkan ke antrian")

    def hitung_waktu_tunggu(self):
        if not self.antrian_biasa and not self.antrian_prioritas:
            print("Tidak ada nasabah didalam antrian")
            return 0
        if self.antrian_prioritas:
            waktu_tunggu = time.time() - self.antrian_prioritas[0].waktu_masuk
        else:
            waktu_tunggu = time.time() - self.antrian_biasa[0].waktu_masuk
        return waktu_tunggu

    def tambah_loket(self, id_loket):
        loket = Loket(id_loket)
        self.lokets.append(loket)
        print(f"Loket {id_loket} Telah ditambahkan.")

    def layani_nasabah(self):
        if self.antrian_prioritas:
            nasabah = self.antrian_prioritas.popleft()  #Ambil dari antrian prioritas
        elif self.antrian_biasa:
            nasabah = self.antrian_biasa.popleft()  #Ambil dari antrian biasa
        else:
            print("Tidak ada nasabah yang perlu dilayani")
            return

        loket = self.lokets[self.loket_index]
        loket.nasabah_dilayani = nasabah
        loket.waktu_mulai = time.time()
        waktu_pelayanan = randint(2, 5)  #Simulasi waktu pelayanan antara 2-5 detik
        print(f"Loket {loket.id_loket} Sedang melayani nasabah '{nasabah.nama}'...")
        time.sleep(waktu_pelayanan)  #Simulasi waktu pelayanan
        self.statistik['total_nasabah'] += 1
        self.statistik['total_waktu'] += (time.time() - loket.waktu_mulai)
        print(f"Nasabah '{nasabah.nama}' Telah dilayani")

        self.loket_index = (self.loket_index + 1) % len(self.lokets) #Update index loket untuk loket berikutnya

    def tampilkan_statistik(self):
        if self.statistik['total_nasabah'] == 0:
            print("Belum ada nasabah yang dilayani")
            return
        rata_rata_waktu = self.statistik['total_waktu'] / self.statistik['total_nasabah']
        print(f"Total nasabah yang dilayani: {self.statistik['total_nasabah']}")
        print(f"Rata-rata waktu tunggu pelayanan: {rata_rata_waktu:.3f} detik")
        
#Penggunaan Antrian Pelayanan
antrian_pelayanan = AntrianPelayanan()

#Penambahan Loket dan Nasabah
antrian_pelayanan.tambah_loket(1)
antrian_pelayanan.tambah_loket(2)
antrian_pelayanan.tambah_loket(3)
antrian_pelayanan.tambah_loket(4)
antrian_pelayanan.tambah_nasabah("Tian", prioritas=True)
antrian_pelayanan.tambah_nasabah("Zwing", prioritas=True)
antrian_pelayanan.tambah_nasabah("Pray")
antrian_pelayanan.tambah_nasabah("Daniel")

#Pelayanan untuk nasabah
antrian_pelayanan.layani_nasabah()
antrian_pelayanan.layani_nasabah()
antrian_pelayanan.layani_nasabah()
antrian_pelayanan.layani_nasabah()

#Statistik Pelayanan
antrian_pelayanan.tampilkan_statistik()