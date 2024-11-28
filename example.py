import random


class MatematikaKuis:
    def __init__(self):
        self.operators = {
            1: ('+', lambda x, y: x + y),
            2: ('-', lambda x, y: x - y),
            3: ('x', lambda x, y: x * y),
            4: (':', lambda x, y: x // max(1, y))
        }

    def tampilan_mulai(self):
        judul = "** Kuis Matematika Sederhana **"
        print("*" * len(judul))
        print(judul)
        print("*" * len(judul))

    def tampilan_menu(self):
        menu = [
            f"{key}. {self.operator_label(key)}" 
            for key in self.operators
        ] + ['5. Exit']
        for item in menu:
            print(item)

    def operator_label(self, key):
        return {
            1: 'Penjumlahan (+)',
            2: 'Pengurangan (-)',
            3: 'Perkalian (x)',
            4: 'Pembagian (:)'
        }.get(key)

    def dapatkan_input_pengguna(self):
        while True:
            try:
                pilihan = int(input('Masukan Pilihan: '))
                if 1 <= pilihan <= 5:
                    return pilihan
                print('Nomor yang dipilih tidak valid. Tolong masukan nomor 1 - 5.')
            except ValueError:
                print('Input tidak valid! Masukan nomor yang valid.')

    def buat_soal_matematika(self, operator_key):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        
        operator_simbol, operator_fungsi = self.operators[operator_key]
        problem = f"{num1} {operator_simbol} {num2}"
        solution = operator_fungsi(num1, num2)
        
        return problem, solution

    def dapatkan_jawaban_pengguna(self, problem):
        print('Masukan jawaban anda: ')
        print(problem, end="")
        return int(input(" = "))

    def periksa_jawaban(self, user_solution, solution):
        if user_solution == solution:
            print('Benar.')
            return 1
        print("Salah.")
        return 0

    def mainkan_kuis(self):
        self.tampilan_mulai()
        self.tampilan_menu()
        print('-' * 24)

        total_soal = 0
        total_benar = 0

        while True:
            pilihan = self.dapatkan_input_pengguna()
            
            if pilihan == 5:
                break

            total_soal += 1
            problem, solution = self.buat_soal_matematika(pilihan)
            user_solution = self.dapatkan_jawaban_pengguna(problem)
            total_benar += self.periksa_jawaban(user_solution, solution)

        print('Keluar dari Kuis.')
        print('-' * 24)
        self.tampilan_hasil(total_soal, total_benar)

    def tampilan_hasil(self, total, benar):
        presentase = round((benar / total * 100), 2) if total > 0 else 0
        print(f"Kamu Menjawab {total} Pertanyaan dengan {benar} benar.")
        print(f"Score kamu {presentase}%. Terimakasih.")

def main():
    kuis = MatematikaKuis()
    kuis.mainkan_kuis()

if __name__ == "__main__":
    main()
