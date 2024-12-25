number = int(input("sonni kiriting: "))#sonni kiriting

i = 0
while i < number:
    i += 1
    if number % i == 0: #bolinuvchilarini topamiz

        print(i, end = " ")