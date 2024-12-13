import random
import matplotlib.pyplot as plt

permintaan = int(input("Max permintaan: "))
permintaan_list = []
for i in range(0, permintaan):
    permintaan_list.append(i)
print("========================================")

frekuensi_list = []
for i in range(permintaan):
    frekuensi = int(input("Frekuensi (hari): "))
    frekuensi_list.append(frekuensi)

def probabilitas(frekuensi_list):
    total_frekuensi = sum(frekuensi_list)
    prob_list = []
    for frekuensi in frekuensi_list:
        prob = frekuensi / total_frekuensi
        prob_list.append(prob)
    return prob_list

def kumulatif(prob_list):
    kumulatif_list = []
    total = 0
    for prob in prob_list:
        total += prob
        kumulatif_list.append(total)
    return kumulatif_list

def interval_bilangan_acak(kumulatif_list):
    interval_list = []
    for i, kumulatif in enumerate(kumulatif_list):
        if i == 0:
            interval_list.append((1, int(kumulatif * 100)))
        else:
            interval_list.append((int(kumulatif_list[i-1] * 100) + 1, int(kumulatif * 100)))
    interval_list[-1] = (interval_list[-1][0], 99)
    return interval_list

def simulasi():
    prob_list = probabilitas(frekuensi_list)
    kumulatif_list = kumulatif(prob_list)
    interval_list = interval_bilangan_acak(kumulatif_list)
    print()

    for i, prob in enumerate(prob_list):
        print(f"Probabilitas frekuensi {frekuensi_list[i]}: {prob:.2f}")
    print()
    for i, prob in enumerate(kumulatif_list):
        print(f"Nilai kumulatif probabilitas: {kumulatif_list[i]:.2f}")
    print()
    for i, prob in enumerate(interval_list):
        print(f"Interval bilangan acak: {interval_list[i][0]} - {interval_list[i][1]}")
    print("========================================")

    perkiraan_permintaan = int(input("Masukkan perkiraan permintaan: "))
    
    hasil_simulasi = []
    for _ in range(0, perkiraan_permintaan):
        bilangan_acak = random.randint(1, 99)
        hasil = 0
        for i, interval in enumerate(interval_list):
            if interval[0] <= bilangan_acak <= interval[1]:
                hasil = permintaan_list[i]
                break
        hasil_simulasi.append((bilangan_acak, hasil))

    print("\nHasil Simulasi:")
    for bilangan_acak, hasil in hasil_simulasi:
        print(f"Bilangan acak: {bilangan_acak}, Permintaan: {hasil}")

    total_permintaan = sum(hasil for _, hasil in hasil_simulasi)
    rata_rata_permintaan = total_permintaan / perkiraan_permintaan if perkiraan_permintaan > 0 else 0
    print(f"\nJumlah seluruh hasil permintaan: {total_permintaan}")
    print(f"Rata-rata permintaan: {rata_rata_permintaan:.2f}")

    hasil = [hasil for _, hasil in hasil_simulasi]
    banyak_permintaan = [hasil.count(i) for i in permintaan_list]

    plt.bar(permintaan_list, banyak_permintaan, color='skyblue', edgecolor='black')
    plt.title("Jumlah Permintaan dari Hasil Simulasi")
    plt.xlabel("Permintaan")
    plt.ylabel("Banyaknya Permintaan")
    plt.xticks(permintaan_list)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    for i, nilai in enumerate(banyak_permintaan):
        plt.text(i, nilai + 1, str(nilai), ha='center', va='bottom')
    plt.show()

simulasi()