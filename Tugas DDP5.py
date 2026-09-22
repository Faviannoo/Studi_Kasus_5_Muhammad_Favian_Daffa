def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000

    biaya = tarif * lama_menginap

    return biaya


print("--- Pemesanan Hotel ---")
print("1. Kamar Standard = Rp200.000/Malam")
print("2. Kamar Deluxe = Rp350.000/Malam")

pilih = int(input("\nPilih Kamar (1/2): "))

if pilih == 1:
    jenis_kamar = "Standard"
elif pilih == 2:
    jenis_kamar = "Deluxe"
else:
    print("\nPilihan Kamar Tidak Tersedia")
while True:
    while True:
        checkin = int(input("\nMasukkan Tanggal Check In: "))
        if 1 <= checkin <= 31:
            break
        else:
            print("\nTanggal Harus antara 1 - 31")
    while True:
        checkout = int(input("\nMasukkan Tanggal Check Out: "))
        if 1 <= checkout <= 31:
            break
        else:
            print("\nTanggal Harus Antara 1 - 31")
    lama_menginap = checkout - checkin
    if lama_menginap > 0:
        break
    else:
        print("\nTanggal Check in dan Check Out Salah")

biaya = hitung_biaya(jenis_kamar, lama_menginap)

print("\n--- Detail Pemesanan ---")
print("Jenis Kamar       :", jenis_kamar)
print("Tanggal Check In  :", checkin)
print("Tanggal Check Out :", checkout)
print("Lama Menginap     :", lama_menginap, "malam")
print("Total Biaya       : Rp", biaya)