def substract(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matriks A dan B harus memiliki ukuran yang sama.")
    
    hasil = []
    
    for i in range(len(A)):  
        baris = [] 
        for j in range(len(A[0])):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris) 
    
    return hasil


A = []
B = []

n = int(input("Masukkan ukuran matriks: "))


print("Matriks A: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)

print("Matriks B: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    B.append(row)

print("\n-- Pengurangan Matriks --")
print("Hasil A - B:")
hasil = substract(A, B)
for baris in hasil:
    print(baris)