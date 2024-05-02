num = [0 for i in range(10)]
hasil = 0

while True:
  i = int(input())
  if (i < 0):
    break
  
  a = str(i)
  for x in a:
    if x == "0":
        num[0] += 1
    elif x == "1":
       num[1] += 1
    elif x == "2":
       num[2] += 1
    elif x == "3":
       num[3] += 1
    elif x == "4":
       num[4] += 1
    elif x == "5":
       num[5] += 1
    elif x == "6":
       num[6] += 1
    elif x == "7":
       num[7] += 1
    elif x == "8":
       num[8] += 1
    elif x == "9":
       num[9] += 1

  hasil += 1


print(hasil)
for i in range(len(num)):
  if i == 9 and num[i] <= 0:
    break
  if num[i] <= 0:
    continue
  print(i, ":", num[i])