def testa():
    cont = 0
    max = 0
    num = int(input("\nInsira o numero que deseja testar: "))
    while num != 1:
        if num % 2 == 0: num = num / 2
        else: num = num * 3 + 1
        cont += 1
        if num > max: max = num
    print(f"\nO pico foi {max}, e esse numero precisou de um total de {cont}\n")

def main():
    s = "s"
    while s == "s":
        testa()
        s = input("Quer tentar outro numero? [s -> sim] \n-> ")

if __name__ == "__main__":
    main()