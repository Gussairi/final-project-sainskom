import numpy as np

def input_matrix():
    n = int(input("Masukkan jumlah status: "))
    print("Masukkan elemen matriks probabilitas transisi (baris per baris):")
    transition_matrix = np.array([list(map(float, input().split())) for _ in range(n)])
    return transition_matrix

def input_initial_state(n):
    print("Masukkan probabilitas awal untuk setiap status:")
    initial_state = np.array(list(map(float, input().split())))
    if len(initial_state) != n:
        raise ValueError("Jumlah elemen dalam probabilitas awal harus sama dengan jumlah status.")
    return initial_state

def calculate_probability(initial_state, transition_matrix, days):
    state = initial_state
    all_states = [state.copy()]
    for _ in range(days):
        state = np.dot(state, transition_matrix)
        all_states.append(state.copy())
    return all_states

def steady_state(transition_matrix, tolerance=1e-6, max_iterations=1000):
    n = len(transition_matrix)
    state = np.ones(n) / n  
    for k in range(max_iterations):
        next_state = np.dot(state, transition_matrix)
        if np.allclose(state, next_state, atol=tolerance):
            return next_state, k + 1
        state = next_state
    return state, max_iterations

transition_matrix = input_matrix()
n = len(transition_matrix)
initial_state = input_initial_state(n)
days = int(input("Masukkan jumlah hari untuk perhitungan: "))

all_probabilities = calculate_probability(initial_state, transition_matrix, days)
print(f"\nProbabilitas untuk setiap hari hingga hari ke-{days}:")
for day, probs in enumerate(all_probabilities):
    print(f"Hari {day}: {', '.join(f'{p:.4f}' for p in probs)}")

steady_state_probs, steady_day = steady_state(transition_matrix)
print("\nKondisi steady state:")
for i, p in enumerate(steady_state_probs):
    print(f"Status {i + 1}: {p:.4f}")
print(f"Steady state mulai tercapai pada hari ke-{steady_day}.")
