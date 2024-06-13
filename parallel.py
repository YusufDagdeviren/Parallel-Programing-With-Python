from multiprocessing import Pool, cpu_count
import time
import sys
def count_characters(substring, char):
    return substring.count(char)

def parallel_count(s):
    n = len(s)
    countA = [0] * n
    countB = [0] * n
    

    # İşlemci havuzu oluşturuyoruz
    with Pool() as pool:
        # "a" karakterleri için paralel hesaplama
        countA = pool.starmap(count_characters, [(s[:i+1], 'a') for i in range(n)])
        # "b" karakterleri için paralel hesaplama
        countB = pool.starmap(count_characters, [(s[:i+1], 'b') for i in range(n)])

    result = [0] * n

    for i in range(n):
        if s[i] == 'a':
            result[i] = countA[i]
        else:
            result[i] = countB[i]

    return result




def main():
    if len(sys.argv) != 2:
        print("Kullanim: python parallel.py <dosya_adi>")
        return

    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as file:
            s = file.read().strip()
    except:
        print(f"Dosya adi bulunamadi: {file_name}")
        return


    start_time = time.time()
    result = parallel_count(s)
    end_time = time.time()

    print("Sonuç: ",result)
    num_cpus = cpu_count()
    print(f"Kullanılan işlemci sayısı: {num_cpus}")
    print("Paralel Algoritma Çalışma Süresi: ",end_time-start_time,"saniye")
    print(f"Maliyet= {(end_time-start_time) * cpu_count()}")


if __name__ == "__main__":
    main()