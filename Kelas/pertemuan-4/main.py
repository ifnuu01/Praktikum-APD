# batas = 20
# for i in range(1, batas, 2):
#     print(f"Perulangan ke-{i}")

# buah_banyak = ["Apel", "Mangga" , "Anggur", "Semangka"]
# for buah in buah_banyak:
#     print(buah)

# for baris in range(1,4):
#     print("Baris ke", baris)
#     for kolom in range(1,4):
#         print(kolom, "kolom", end=" ")
#     print()
#     print()

# lagi = "yes"
# ulang = 0
# while lagi == "yes":
#     ulang += 1
#     print("Mabar")
#     lagi = input("Mabar lagi gk?")
# print("Selesai Mabar!")
# print(f"Perulangan terjadi sebanyak {ulang} kali")

# for i in range(1,10):
#     if i == 5:
#         break
#     else:
#         print(f"Perulangan ke-{i}")
# buah_banyak = ["Apel", "Mangga" , "Anggur", "Semangka"]
# for buah in buah_banyak:
#     if buah == "Anggur":
#         print("Buah anggur ketemu")
#         break
#     else:
#       print("Belum ketemu")

# while True:
#     ulang = input("Mabar lagi: ")
#     if ulang.lower() == "gk":
#         break
#     print("Mabar lagi")

# for i in range(1, 10):
#     if i % 2 == 1:
#         continue
#     print(f"Perulangan ke-{i}")

# batas = 5
# print("Matrix")
# for i in range(batas):
#   print("* " * batas)

# print("Segitiga Siku-Siku")
# for i in range(1, 5):
#   print("* " * i)

# print("Segitiga Sama Kaki")
# for i in range(batas):
#   print(" " * (batas - i )+ "*" *(2 * i -1))

# for i in range(5) :
#     for j in range(5) :
#         print("*" , end="hello")
#     print()

kesempatan = 3

while kesempatan > 0:
  username = input("Masukkan username: ")
  nim = input("Masukkan password: ")

  if username == "admin" and nim == "admin#1234":
    print("Berhasil login")
    break
  else:
    print("Username atau password salah!")
    kesempatan -= 1
    print(f"Kesempatan login tersisa {kesempatan} kali")

print("Program utama")