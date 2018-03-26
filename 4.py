import kurs
import andrew



def main():
    rate = int(input("Vvedite procentnyu stavky: "))
    money = int(input("Vvedite summy: "))
    period = int(input("Vvedite period vedeniya scheta v mesacah: "))

    result = andrew.calculate_income(rate,money,period)
    print("Parametry sceta: \n", "Symma: ", money, "\n", "Stavka: ", rate, "\n", "Period: ", period, "\n", "Symma na schete v konce perioda: ", result)

if __name__ == "__main__":
    main()

