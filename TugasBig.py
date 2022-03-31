class Node(object):
    def _init_(self,initdata):
        self.data = initdata
        self.next = None

    def getData (self) :
        return self.data

    def getNext (self,newdata) :
        self.data = newdata

    def setNext (self,newnext) :
        self.next = newnext


class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0

    def __compress(self):
        newlst = []
        for i in range(self.frontIdx, len(self.items)):
            newlst.append(self.items[i])
        self.items = newlst
        self.frontIdx = 0

    def isEmpty(self):
        return self.frontIdx == len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty queue")

        return self.items[self.frontIdx]

def mainmenu():
    print("===========================================\n")
    print("         --Cinema Indo Studio 5--")
    print("         1. pilih waktu menonton")
    print("       2. pilih genre dan judul film")
    print("          3. pilih tempat duduk")
    print("            4. tampilkan data\n")
    print("===========================================")

def backorhome():
    key2 = str(input('Apakah ingin kembali ke menu awal? (Y/N)\n'))
    if key2 == 'Y' or key2 == 'y':
        print('\n')
        return True
    else:
        print('Aplikasi akan ditutup terimakasih telah menggunakan aplikasi kami')
        exit(0)


queuepemesanan = Queue()
barangfull = set()
harga = 0
HargaTiket = {'pagi' : 20000, 'siang' : 25000, 'malam' : 30000}
keteranganNoKursi = ["NK 1", "NK 2", "NK 3", "NK 4", "NK 5", "NK 6", "NK 7", "NK 8", "NK 9", "NK 10"]
genrefilm = ["1.comedy\n","2.romance","3.horror","4.thriller","5.action","6.khusus18"]
comedy = ["1.insidious","2.jigsaw","3.chucky","4.demon house"]
romance = ["1.dark amazon","2.sleeper","3.blackmail","4.a quite place"]
horror = ["1.mr.bean","2.jangkrik bos","3.dilan 1990"]
thriller = ["1.cinderella","2.i love u","3.love simon","4.be my slave"]
action = ["1.point blank movie","2.dota movie","3.lost saga season 1","4.dragonest : capture the dragon"]
khusus18 = ["1.surga ditelapak kaki ibu","2.siksa kubur","3.pedihnya api neraka"]
pagi = ["pagi       : 1. 06:00", "2. 08:00","3. 10:00"]
siang = ["siang     : 1.  12:00", "2.  14:00,", "3.  16:00", "4.  18:00"]
malam = ["malam     : 1.  20:00", "2.  22:00", "3.  24:00"]

if __name__ == '__main__':
    nama = input("Masukkan Nama Anda   :   ")
    print("WELCOME")
    print(nama)
    print("Silahkan Pilih Menu Yang Tersedia")
    while True:
        mainmenu()
        Pilihan = int(input('Masukkan Pilihan anda   :   '))
        if Pilihan == 1 :
            while True:
                print(HargaTiket)
                print("===========================================")
                x = input("masukaan Pilihan Anda : ")
                if x in HargaTiket :
                    queuepemesanan.enqueue(x)
                    harga += HargaTiket[x]
                    print('Harga tiket  adalah    :   ', harga)
                    print("waktu menonton dapat dilakukan pada jam-jam berikut :")
                    print(pagi)
                    print(siang)
                    print(malam)
                else:
                    print('\nwaktu yang anda pilih tidak ada!perhatikan capslok anda, Silahkan coba lagi\n')
                    continue
                break

        elif Pilihan == 2 :
            while True:
                print("===========================================")
                print(genrefilm)
                print("===========================================")
                x = int(input("masukaan Nomor Pilihan Anda : "))
                x = x - 1
                print("===========================================")
                print(genrefilm[x])
                judulgenre = (genrefilm[x])
                y = x+1
                if (y == 1):
                    print("===========================================")
                    print (comedy)
                    print("===========================================")
                    z = int(input("masukkan nomor judul  film pilihan anda  : "))
                    z = z-1
                    print("===========================================")
                    print(comedy[z])
                    print("===========================================")
                    judulfilm = comedy[z]
                    back = input('Apakah anda ingin merubah? (Y/N)   :   ')
                    if back == 'y' or back == 'Y':
                        continue
                    elif back == 'n' or back == 'N':
                        break
                elif (y == 2):
                    print("===========================================")
                    print(romance)
                    print("===========================================")
                    z = int(input("masukkan nomor judul  film pilihan anda  : "))
                    z = z - 1
                    print("===========================================")
                    print(romance[z])
                    print("===========================================")
                    judulfilm = romance[z]
                    back = input('Apakah anda ingin merubah? (Y/N)   :   ')
                    if back == 'y' or back == 'Y':
                        continue
                    elif back == 'n' or back == 'N':
                        break
                elif (y == 3):
                    print("===========================================")
                    print(horror)
                    print("===========================================")
                    z = int(input("masukkan nomor judul  film pilihan anda  : "))
                    z = z - 1
                    print("===========================================")
                    print(horror[z])
                    print("===========================================")
                    judulfilm = horror[z]
                    back = input('Apakah anda ingin merubah? (Y/N)   :   ')
                    if back == 'y' or back == 'Y':
                        continue
                    elif back == 'n' or back == 'N':
                        break
                elif (y == 4):
                    print("===========================================")
                    print(thriller)
                    print("===========================================")
                    z = int(input("masukkan nomor judul  film pilihan anda  : "))
                    z = z - 1
                    print("===========================================")
                    print(thriller[z])
                    print("===========================================")
                    judulfilm = thriller[z]
                    back = input('Apakah anda ingin merubah? (Y/N)   :   ')
                    if back == 'y' or back == 'Y':
                        continue
                    elif back == 'n' or back == 'N':
                        break
                elif (y == 5):
                    print("===========================================")
                    print(action)
                    print("===========================================")
                    z = int(input("masukkan nomor judul  film pilihan anda  : "))
                    z = z - 1
                    print("===========================================")
                    print(action[z])
                    print("===========================================")
                    judulfilm = action[z]
                    back = input('Apakah anda ingin merubah? (Y/N)   :   ')
                    if back == 'y' or back == 'Y':
                        continue
                    elif back == 'n' or back == 'N':
                        break
                elif (y == 6):
                    print("===========================================")
                    print(khusus18)
                    print("===========================================")
                    z = int(input("masukkan nomor judul  film pilihan anda  : "))
                    z = z - 1
                    print("===========================================")
                    print(khusus18[z])
                    print("===========================================")
                    judulfilm = khusus18[z]
                    back = input('Apakah anda ingin merubah? (Y/N)   :   ')
                    if back == 'y' or back == 'Y':
                        continue
                    elif back == 'n' or back == 'N':
                        break
                else:
                    print("===========================================")
                    print('Pilihan anda tidak ada')
                    continue

        elif Pilihan == 3 :
            print(keteranganNoKursi)
            x = int(input("masukkan nomor kursi yang anda inginkan  : "))
            x= x-1
            print(keteranganNoKursi[x])


        elif Pilihan == 4 :
            print("==============================================================================================")
            print("                           Welcome To Cinema Indo Studio 5--            ")
            print("")
            print("Nama                                 :",nama)
            print("Genre film                           :",judulgenre)
            print("judul film                           :",judulfilm)
            print("Nomor Kursi                          : ", keteranganNoKursi[x])
            print("Harga tiket                          :", harga)
            print("")
            print("                                                             Terimakasih Atas Kepercayaan Anda")
            print("                                                                     selamat menikmati")
            print("==============================================================================================")
            break


        else:
            print("===========================================")
            print('Pilihan anda tidak ada,silahkan coba lagi')
            continue



