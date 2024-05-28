import numpy as np
import time

# Nama : Leonardus Deni Prabowo
# NIM : 21120122120012
# Metode Numerik - Kelas A
# Integrasi Numerik Mencari Nilai Pi

# Fungsi Yang Diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode Integrasi Riemann
def riemann_integral(f, a, b, n):
    width = (b - a) / n
    total = 0.0
    for i in range(n):
        total += f(a + i * width) * width
    return total

# Menghitung Galat RMS Reimann - Referensi
def rms_error_Reimann_Referensi(estimated_pi_reimann, reference_pi):
    return np.sqrt(np.mean((estimated_pi_reimann - reference_pi)**2))

# Referensi Nilai Pi
pi_ref = 3.14159265358979323846

# Nilai N
N_values = [10, 100, 1000, 10000]

# Plot Testing
for N in N_values:
    start_time = time.time()
    estimated_pi_reimann = riemann_integral(f, 0, 1, N)
    execution_time = time.time() - start_time
    error_reimann_ref = rms_error_Reimann_Referensi(estimated_pi_reimann, pi_ref)
    
    print(f"Nilai N = {N}")
    print(f"Estimasi Nilai Pi Reimann: {estimated_pi_reimann}")
    print(f"RMS Error Reimann-Referensi (Galat): {error_reimann_ref}")
    print(f"Waktu Eksekusi: {execution_time} Detik")
    print("-" * 30)
