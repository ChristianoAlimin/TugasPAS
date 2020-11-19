from os import system
from json import dump, load
from datetime import datetime

def print_menu():
	system("cls")
	print("""
	Penyimpanan Kontak Sederhana
	[1]. Lihat Daftar Tiket Tersedia
	[2]. Menambahkan tiket (BOOKING)
	[3]. Mencari informasi tiket
	[4]. Menghapus/Membatalkan tiket
	[5]. Mengubah Informasi tiket
	[6]. Tentang Aplikasi
	[Q]. Keluar
		""")

def print_header(msg):
	system("cls")
	print(msg)

def not_empty(container):
	if len(container) !=0:
		return True
	else:
		return False

def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(id_tiket=None, maskapai=True, kursi=True, all_data=False):
	if id_tiket != None and all_data == False:
		print(f"ID : {id_tiket}")
		print(f"DESTINASI : {tikets[id_tiket]['destinasi']}")
		print(f"MASKAPAI : {tikets[id_tiket]['maskapai']}")
		print(f"KURSI : {tikets[id_tiket]['kursi']}")
	elif kursi == False and all_data == False:
		print(f"ID : {id_tiket}")
		print(f"DESTINASI : {tikets[id_tiket]['destinasi']}")
		print(f"MASKAPAI : {tikets[id_tiket]['maskapai']}")
	elif all_data == True:
		for id_tiket in tikets:# lists, string, dict
			destinasi = tikets[id_tiket]["destinasi"]
			maskapai = tikets[id_tiket]["maskapai"]
			kursi = tikets[id_tiket]["kursi"]
			print(f"ID : {id_tiket} - DESTINASI : {destinasi} - MASKAPAI : {maskapai} - KURSI : {kursi}")

def view_tikets():
	print_header("DAFTAR TIKET TERSEDIA")
	if not_empty(tikets):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA TIKET TERSEDIA")
	input("Tekan ENTER untuk kembali ke MENU")

def create_id_tiket(ticket, plane):
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day

	counter = len(tikets) + 1
	first = ticket[0].upper()
	last_4 = plane[-4:]
	
	id_tiket = ("%04d%02d%02d-C%03d%s%s" % (tahun, bulan, hari, counter, first, last_4))
	return id_tiket

def add_tiket():
	print_header("MENAMBAHKAN TIKET BARU")
	destinasi = input("DESTINASI \t: ")
	maskapai = input("MASKAPAI \t: ")
	kursi = input("KURSI \t: ")
	respon = input(f"Apakah yakin ingin menambahkan tiket : {destinasi} ? (Y/N) ")
	if verify_ans(respon):
		id_tiket = create_id_tiket(ticket=destinasi, plane=maskapai)
		tikets[id_tiket] = {
			"destinasi" : destinasi,
			"maskapai" : maskapai,
			"kursi" : kursi
		}
		saved= save_data_tikets()
		if saved:
			print("Data Tiket Tersimpan.")
		else:
			print("Kesalahan saat menyimpan")
	else:
		print("Data Batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def searching_by_destinasi(tiket):
	for id_tiket in tikets:
		if tikets[id_tiket]['destinasi'] == tiket:
			return id_tiket
	else:
		return False

def find_tiket():
	print_header("MENCARI TIKET")
	destinasi = input("Destinasi tiket yang Dicari : ")
	exists = searching_by_destinasi(destinasi)
	if exists:
		print("Data Ditemukan")
		print_data(id_tiket=exists)
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def delete_tiket():
	print_header("MENGHAPUS TIKET")
	destinasi = input("Destinasi Tiket yang akan Dihapus : ")
	exists = searching_by_destinasi(destinasi)
	if exists:
		print_data(id_tiket=exists)
		respon = input(f"Yakin ingin mengapus {destinasi} ? (Y/N) ")
		if verify_ans(respon):
			del tikets[exists]
			saved= save_data_tikets()
			if saved:
				print("Data Tiket Telah Dihapus.")
			else:
				print("Kesalahan saat menyimpan")
		else:
			print("Data Tiket Batal Dihapus")
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def update_tiket_destinasi(id_tiket):
	print(f"Destinasi Lama : {tikets[id_tiket]['destinasi']}")
	new_destinasi = input("Masukkan Destinasi baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tikets[id_tiket]['destinasi'] = new_destinasi
		print("Data Telah di simpan")
		print_data(id_tiket)
	else:
		print("Data Batal diubah")

def update_tiket_maskapai(id_tiket):
	print(f"Maskapai Lama : {tikets[id_tiket]['maskapai']}")
	new_maskapai = input("Masukkan Maskapai Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result:
		tikets[id_tiket]['maskapai'] = new_maskapai
		print("Data Telah di simpan")
		print_data(id_tiket)
	else:
		print("Data Batal diubah")

def update_tiket_kursi(tiket):
	print(f"Kursi Lama : {tikets[tiket]['kursi']}")
	new_kursi = input("Masukkan Kursi Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result:
		tikets[tiket]['kursi'] = new_kursi
		print("Data Telah di simpan")
		print_data(tiket)
	else:
		print("Data Batal diubah")

def update_tiket():
	print_header("MENGUPDATE INFO TIKET")
	destinasi = input("Destinasi yang akan di-update : ")
	exists = searching_by_destinasi(destinasi)
	if exists:
		print_data(exists)
		print("EDIT FIELD [1] DESTINASI - [2] MASKAPAI - [3] KURSI")
		respon = input ("MASUKAN PILIHAN (1/2/3) : ")
		if respon == "1":
			update_tiket_destinasi(exists)
		elif respon == "2":
			update_tiket_maskapai(exists)
		elif respon == "3":
			update_tiket_kursi(exists)
		saved = save_data_tikets()
		if saved:
			print("Data Tiket Telah di-update.")
		else:
			print("Kesalahan saat menyimpan")
	
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def tent_app():
	print_header("App ini dibuat untuk memudahkan pengguna dalam menyimpan, mencari, menambah, dan menghapus data tiket pesawat yang ada")
	input("Tekan ENTER untuk kembali ke MENU")
	
def check_user_input(char):
	char = char.upper()
	if char == "Q":
		print("BYE!!!")
		return True
	elif char == "1":
		view_tikets()
	elif char == "2":
		add_tiket()
	elif char == "3":
		find_tiket()
	elif char == "4":
		delete_tiket()
	elif char == "5":
		update_tiket()
	elif char == "6":
		tent_app()

def load_data_tikets():
	with open(file_path, 'r') as file:
		data = load(file)
	return data

def save_data_tikets():
	with open(file_path, 'w') as file:
		dump(tikets, file)
	return True

#flag/sign/tanda menyimpan sebuah kondisi
stop = False
file_path = "filetxt/tikets.json"
tikets = load_data_tikets()
while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)
