from collections import defaultdict

def map_function(text):
    for word in text.split():
        yield (word, 1)

def reduce_function(pairs):
    result = defaultdict(int)
    for word, count in pairs:
        result[word] += count
    return result

# Fungsi untuk membaca file teks
fileku = r"C:\Users\Administrator\Downloads\MANDO.txt"
with open(fileku, 'r') as file:
    teks = file.read()

gabungan = map_function(teks)
hasil = reduce_function(gabungan) 

for word, count in hasil.items():
    print('jumlah perulangan kata :')
    print(f'{word}: {count}')
