# Soal Nomor 2
print("--- Nomor 2 ---")
def cek_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 60 <= nilai <=70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai Tidak Valid" 

# Pemanggilan
print(cek_kelulusan(65))
