def input_data():
    nim = input("Masukkan NIM anda: ")
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    return nim, uts, uas

def main():
    for i in range(2):
        print("Data Ke-{}".format(i+1))
        nim, uts, uas = input_data()
        print("NIM anda adalah {}, nilai UTS anda {}, nilai UAS anda {}".format(nim, uts, uas))

if __name__ == "__main__":
    main()
