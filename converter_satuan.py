isUlangi = 'y'
list_satuan = ["mm", "cm", "dm", "m", "dam", "hm", "km"]

print("Konversi Satuan Panjang")

def convert(x, satuan):
    letak = 0
    x = float(x)
    # CHECK SATUAN BERADA DI TINGKAT MANA
    for i in range(len(list_satuan)):
        if list_satuan[i] == satuan:
            letak = i
    
    for i in range(len(list_satuan)):
        if i == letak:
            hasil = "{:,.0f}".format(x)
            print(list_satuan[i], " = ", hasil)
            
        # KONVERSI KE ATAS
        elif i > letak:
            hasil = "{:,}".format(x / pow(10, i - letak))
            print(list_satuan[i], " = ", hasil)
            
        # KONVERSI KE BAWAH
        elif i < letak:
            hasil = "{:,.0f}".format(x * pow(10, letak - i))
            print(list_satuan[i], " = ", hasil)

while isUlangi == 'y':
    angka = input("Input Angka : ")

    print("Pilih Satuan -> [mm, cm, dm, m, dam, hm, km]")
    satuan = input("Input Satuan : ")

    while satuan not in list_satuan:
        satuan = input("Ulangi Input Satuan : ")

    convert(angka, satuan)
    isUlangi = input("\nExit? [y/n]: ")

print("[EXIT]")