raqam = int(input("sonni kiriting: "))
count = 0
i = 2
while i < raqam:
    
    for raq in range (1, i + 1):
        
        if i % raq == 0:
            count += 1
            
    if count <= 2:
        print(i, end = " ")
        count = 0
        
    count = 0
    i += 1