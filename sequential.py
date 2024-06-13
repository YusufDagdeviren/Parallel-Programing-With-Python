import time
import sys
def sequential_count(s):
    n = len(s)
    countA = [0] * n
    countB = [0] * n
    result = [0] * n

    for i in range(n):
        if i == 0:
            countA[i] = 1 if s[i] == 'a' else 0
            countB[i] = 1 if s[i] == 'b' else 0
        else:
            countA[i] = countA[i-1] + (1 if s[i] == 'a' else 0)
            countB[i] = countB[i-1] + (1 if s[i] == 'b' else 0)
        for i in range(n):
            if s[i] == 'a':
                result[i] = countA[i]
            else:
                result[i] = countB[i]
    return result


def main():

    if len(sys.argv) != 2:
        print("Kullanim: python sequential.py <dosya_adi>")
        return
    
    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as file:
            s = file.read().strip()
    except:
        print(f"Dosya adi bulunamadi: {file_name}")

    start_time = time.time()
    result = sequential_count(s)
    end_time = time.time()

    print("Sonuç: ",result)
    print("Ardışıl Algoritma Çalışma Süresi: ",end_time-start_time,"saniye")


if __name__ == "__main__":
    main()
    
