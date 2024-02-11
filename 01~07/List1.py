animals = ["개", "고양이", "사자", "말", "원숭이"]

animals[0] = "쥐"

print(len(animals).__str__() + "종류의 동물이 리스트에 있습니다.")
print(animals)

animals.append("여우")

print(animals)

animals.pop(5)

print(animals)

animals.remove("말")

print(animals)

animals.sort()

print(animals)

if "염소" in animals:
    print("염소가 리스트에 있습니다.")

elif "염소" not in animals:
    print("염소가 리스트에 없습니다.")
    answer = input("추가하시겠습니까 (y/n) ?")    
    if answer == "y":
        animals.append("염소")
        print(animals)
    elif answer == "n":
        print("프로그램을 종료합니다.")