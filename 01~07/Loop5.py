animals = []

userinput = " "

print("animals 리스트를 만들어봅시다.")
print("한 번에 하나씩 동물을 입역하세요.")
print("입력을 끝내려면 빈칸을 입력하세요.")

while userinput != "":
    userinput = input("동물의 종류를 입력하세요. 끝내려면 빈칸을 입력하세요 : ").strip()
    if len(userinput) > 0:
        animals.append(userinput)

animals.sort()

print(animals)