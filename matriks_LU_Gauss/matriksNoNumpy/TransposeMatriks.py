def transpose(A):
    hasil = [list(baris) for baris in zip(*A)]
    return hasil

A = []

n = int(input("Masukkan ukuran matriks: "))


print("Matriks A: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)

print("\n-- Transpose Matriks --")
print("Transpose Matriks A:")
hasil = transpose(A)
for baris in hasil:
    print(baris)
