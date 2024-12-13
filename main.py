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
    print("6. Linear + Kuadratic Interpolation")
    print("7. Polinom Newton")
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
