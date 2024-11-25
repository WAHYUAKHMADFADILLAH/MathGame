import random as r

print("===========================================")
print("====selamat datang di game berhitung!!====")
print("===========================================")
print(('Tingkat Kesulitan menggunakan nomor berapapun! contoh = 4 '))
def main():
    while True:
        try:
            kesulitan = int(input("Masukan Tingkat kesulitan : ").strip())
        except ValueError:
            print('Tingkat kesulitan hanya berupa angka!!')
            return

        no1 = r.randrange(1, kesulitan + 1)
        no2 = r.randrange(1, kesulitan + 1)

        hasil = (no1 * kesulitan) + (no2 * kesulitan)
        try:
           jawab = int(input(f'{no1 * kesulitan} + {no2 * kesulitan} = '))
           if jawab == hasil:
               print('Benar!!')
           else:
               print("Salah!!")
        except ValueError:
            print('Masukan Hanya angka!!')

        Keluar = str(input("Lanjut?? [y/n]: ").strip().lower())
        if Keluar == "n":
            print("===========================")
            print("Terimakasih telah bermain!")
            print("===========================")
            break
        


if __name__ == "__main__":
    main()
