i = 0

while True:
    i += 1
    
    if i == 51:
        break

    if not(i % 3 == 0):
        continue
    
    print(i)
