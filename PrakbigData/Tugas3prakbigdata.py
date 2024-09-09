from collections import defaultdict

# Fungsi untuk membaca file CSV
def read_file(file_path):
    with open(file_path, 'r') as file:
        # Baca setiap baris dan pisahkan berdasarkan koma (CSV)
        text_data = [line.strip().split(',') for line in file.readlines()]
    return text_data

# Fungsi untuk memetakan setiap baris menjadi pasangan (nama_atlet, berat_badan)
def map_function(row):
    athlete = row[0].strip()
    weight = float(row[1].strip())
    return [(athlete, weight)]

# Fungsi untuk menggabungkan total berat badan dan jumlah atlet untuk setiap atlet
def reduce_function(mapped_data):
    athlete_data = defaultdict(lambda: {'total_weight': 0, 'count': 0})
    for athlete, weight in mapped_data:
        athlete_data[athlete]['total_weight'] += weight
        athlete_data[athlete]['count'] += 1
    return athlete_data

# Path ke file CSV
file_path = r"C:\Users\Administrator\Downloads\atlitboxing.csv"  # Sesuaikan dengan lokasi file Anda

# Membaca data dari file
text_data = read_file(file_path)

# Langkah Map: Memetakan setiap baris menjadi pasangan (nama_atlet, berat_badan)
mapped_data = []
for row in text_data[1:]:  # Skip header baris pertama
    mapped_data.extend(map_function(row))

# Langkah Reduce: Menghitung total berat badan dan jumlah atlet
athlete_data = reduce_function(mapped_data)

# Menghitung rata-rata berat badan untuk setiap atlet
average_weights = {athlete: data['total_weight'] / data['count'] for athlete, data in athlete_data.items()}

# Menampilkan hasil rata-rata berat badan per atlet
print("Nama Atlet | Rata-rata Berat Badan (kg)")
print("-" * 40)
for athlete, avg_weight in average_weights.items():
    print(f"{athlete}: {avg_weight:.2f}")

# Menampilkan total rata-rata berat badan
overall_avg_weight = sum(athlete_data[athlete]['total_weight'] for athlete in athlete_data) / sum(athlete_data[athlete]['count'] for athlete in athlete_data)
print(f"\nRata-rata Berat Badan Keseluruhan: {overall_avg_weight:.2f} kg")
