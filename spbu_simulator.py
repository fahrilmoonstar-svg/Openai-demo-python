print("----- SISTEM SPBU -----")

print("\nPilih Jenis BBM")
print("1. Pertalite       (Rp10.000/L)")
print("2. Pertamax       (Rp16.250/L)")
print("3. Pertamax Turbo  (Rp19.300/L)")

pilihan = input("\nMasukkan pilihan (1/2/3): ")

if pilihan == "1":
    bbm = "Pertalite"
    harga = 10000
elif pilihan == "2":
    bbm = "Pertamax"
    harga = 16250
elif pilihan == "3":
    bbm = "Pertamax Turbo"
    harga = 19300
else:
    print("\nPilihan tidak tersedia!")
    exit()

nominal = int(input("\nMasukkan nominal pembelian (Rp): "))

liter = nominal / harga

print("\n========== STRUK PEMBELIAN ==========")
print("Jenis BBM        :", bbm)
print("Harga/Liter      : Rp{:.0f}".format(harga).replace(",", "."))
print("Nominal Bayar    : Rp{:.0f}".format(nominal).replace(",", "."))
print("BBM Didapat      : {:.2f} Liter".format(liter))
print("=====================================")

print("\nTerima kasih telah menggunakan layanan SPBU.")