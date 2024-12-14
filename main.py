import os
import subprocess
import sys

def run_file(file_path):
    try:
        subprocess.run([sys.executable, file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {file_path}: {e}")

def display_menu():
    print("\nMenu:")
    print("1. Monte Carlo")
    print("2. Persamaan Non-Linear ")
    print("3. Iterasi Gauss Seidel")
    print("4. Iterasi Jacobi")
    print("5. Markov Chain")
    print("6. Linear + Quadratic Interpolation")
    print("7. Polinom Newton")
    print("8. Eliminasi Gauss")
    print("9. LU Decomposition")
    print("10. Pertambahan Matriks")
    print("11. Pengurangan Matriks")
    print("12. Perkalian Matriks")
    print("13. Perkalian Skalar Matriks")
    print("14. Transpose Matriks")
    print("15. Determinant Matriks")
    print("16. Inverse Matriks")
    print("17. Trace Matriks")
    print("18. Pertambahan Matriks Numpy")
    print("19. Pengurangan Matriks Numpy")
    print("20. Perkalian Matriks Numpy")
    print("21. Perkalian Skalar Matriks Numpy")
    print("22. Transpose Matriks Numpy")
    print("23. Determinant Matriks Numpy")
    print("24. Inverse Matriks Numpy")
    print("25. Trace Matriks Numpy")
    print("0. Exit")

def main():
    file_paths = {
        1: "monte_carlo\MonteCarlo.py",
        2: "monte_carlo\PersNonLinier.py",
        3: "markov_iterasi\iterasiGaussSeidel.py",
        4: "markov_iterasi\iterasiJacobi.py",
        5: "markov_iterasi\markovChain.py",
        6: "interpolation\linearQuadraticInterpolation.py",
        7: "interpolation\polinomNewton.py",
        8: "matriks_LU_Gauss\eliminasi_gauss.py",
        9: "matriks_LU_Gauss\LU_Decomposition.py", 
        10: "matriks_LU_Gauss\matriksNoNumpy\pertambahanMatriks.py",
        11: "matriks_LU_Gauss\matriksNoNumpy\penguranganMatriks.py",
        12: "matriks_LU_Gauss\matriksNoNumpy\perkalianMatriks.py",
        13: "matriks_LU_Gauss\matriksNoNumpy\scalarMatriks.py",
        14: "matriks_LU_Gauss\matriksNoNumpy\TransposeMatriks.py",
        15: "matriks_LU_Gauss\matriksNoNumpy\determinantMatriks.py",
        16: "matriks_LU_Gauss\matriksNoNumpy\inverseMatriks.py",
        17: "matriks_LU_Gauss\matriksNoNumpy\TraceMatriks.py",
        18: "matriks_LU_Gauss\matriksNumpy\pertambahanMatriks.py",
        19: "matriks_LU_Gauss\matriksNumpy\penguranganMatriks.py",
        20: "matriks_LU_Gauss\matriksNumpy\perkalianMatriks.py",
        21: "matriks_LU_Gauss\matriksNumpy\scalarMatriks.py",
        22: "matriks_LU_Gauss\matriksNumpy\TransposeMatriks.py",
        23: "matriks_LU_Gauss\matriksNumpy\determinantMatriks.py",
        24: "matriks_LU_Gauss\matriksNumpy\inverseMatriks.py",
        25: "matriks_LU_Gauss\matriksNumpy\TraceMatriks.py",


    }

    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 0:
                print("Exiting...")
                break
            elif choice in file_paths:
                file_path = file_paths[choice]
                print(f"\nRunning {os.path.basename(file_path)}...\n")
                run_file(file_path)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
