def testa():
    count = 0
    max = 0
    num = int(input("\nInsert the number you want to try: "))
    while num != 1:
        if num % 2 == 0: num = num / 2 # applies the Collatz Conjecture
        else: num = num * 3 + 1
        count += 1 # increases steps taken
        if num > max: max = num # stores max value reached
    print(f"\nHighest number reached was {max}, and it needed {count} steps until it reached 1.\n")

def main():
    s = "y"
    while s == "y":
        testa()
        s = input("Want to try another number? [y -> yes] \n-> ")

if __name__ == "__main__":
    main()