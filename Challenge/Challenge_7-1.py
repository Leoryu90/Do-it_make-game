animals = []

userinput = " "

print("animals 리스트를 만들어봅시다.")
print("한 번에 하나씩 동물을 입력하세요.")
print("입력을 끝내려면 빈칸을 입력하세요.")

#기존 작업물
"""
while userinput != "":
    userinput = input("동물의 종류를 입력하세요. 끝내려면 빈칸을 입력하세요 : ").strip()
    if userinput in animals:
        userinput = input("이미 리스트에 있습니다. 다른 동물의 종류를 입력하세요. 끝내려면 빈칸을 입력하세요 : ").strip()
        if len(userinput) > 0:
            animals.append(userinput)

    elif len(userinput) > 0:
        animals.append(userinput)
"""

# 카페에서 도움 준 코드
"""
while True:
    userinput = input("동물의 종류를 입력하세요. 끝내려면 빈칸을 입력하세요: ").strip()
    if userinput == "":
        break
    if userinput in animals:
        print("이미 리스트에 있습니다. 다른 동물의 종류를 입력하세요.")
        continue
"""

#합친 결과물
while True:
    userinput = input("동물의 종류를 입력하세요. 끝내려면 빈칸을 입력하세요 : ").strip()
    if userinput == "":
        break

    elif userinput in animals:
        print("이미 리스트에 있습니다. 다른 동물의 종류를 입력하세요.")
        continue

    else:
        animals.append(userinput)

animals.sort()

for animal in animals:
    print(animal)