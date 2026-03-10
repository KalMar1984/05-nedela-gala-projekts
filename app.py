from storage import load_expenses, save_expenses  
# Importē funkcijas datu ielādei un saglabāšanai

from logic import sum_total  
# Importē funkciju kopējās summas aprēķināšanai

from datetime import date  
# Importē bibliotēku, kas ļauj iegūt šodienas datumu


CATEGORIES = [  
    # Saraksts ar izdevumu kategorijām
    "Ēdiens",
    "Transports",
    "Izklaide",
    "Komunālie maksājumi",
    "Veselība",
    "Iepirkšanās",
    "Cits"
]


def add_expense(expenses):  
    # Funkcija jauna izdevuma pievienošanai

    today = str(date.today())  
    # Iegūst šodienas datumu un pārvērš to par tekstu

    user_date = input(f"Datums (YYYY-MM-DD) [{today}]: ")  
    # Prasa lietotājam ievadīt datumu

    if user_date == "":  
        # Pārbauda vai lietotājs neko neievadīja

        user_date = today  
        # Ja tukšs, izmanto šodienas datumu

    print("Kategorija:")  
    # Izdrukā tekstu terminālī

    for i, cat in enumerate(CATEGORIES, 1):  
        # enumerate piešķir katrai kategorijai numuru (sākot no 1)

        print(f"{i}) {cat}")  
        # Izdrukā kategoriju ar tās numuru

    cat_index = int(input("Izvēlies (1-7): ")) - 1  
    # Lietotājs ievada kategorijas numuru
    # -1 nepieciešams, jo saraksta indekss sākas no 0

    category = CATEGORIES[cat_index]  
    # No saraksta paņem izvēlēto kategoriju

    amount = float(input("Summa (EUR): "))  
    # Lietotājs ievada summu un tā tiek pārvērsta par skaitli

    description = input("Apraksts: ")  
    # Lietotājs ievada īsu aprakstu

    expense = {  
        # Izveido jaunu vārdnīcu ar izdevuma datiem
        "date": user_date,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)  
    # Pievieno jauno izdevumu sarakstam

    save_expenses(expenses)  
    # Saglabā izdevumu sarakstu JSON failā

    print(f"✓ Pievienots: {user_date} | {category} | {amount} EUR | {description}")  
    # Parāda paziņojumu, ka izdevums pievienots


def show_expenses(expenses):  
    # Funkcija izdevumu parādīšanai

    if len(expenses) == 0:  
        # Pārbauda vai saraksts ir tukšs

        print("Nav neviena izdevuma.")  
        # Ja tukšs, parāda ziņu

        return  
        # Beidz funkciju

    print("\nDatums       Summa    Kategorija   Apraksts")  
    # Izdrukā tabulas virsrakstu

    print("-" * 50)  
    # Izdrukā atdalīšanas līniju

    for e in expenses:  
        # Iet cauri visiem izdevumiem

        print(f"{e['date']}  {e['amount']:6.2f}  {e['category']:12} {e['description']}")  
        # Izdrukā vienu izdevuma rindu

    print("-" * 50)  
    # Izdrukā tabulas apakšējo līniju

    print("Kopā:", sum_total(expenses), "EUR")  
    # Parāda kopējo summu


def main():  
    # Galvenā programmas funkcija

    expenses = load_expenses()  
    # Ielādē izdevumus no JSON faila

    while True:  
        # Bezgalīgs cikls izvēlnei

        print("\n1) Pievienot izdevumu")  
        print("2) Parādīt izdevumus")  
        print("7) Iziet")

        choice = input("\nIzvēlies: ")  
        # Lietotājs ievada izvēles numuru

        if choice == "1":  
            add_expense(expenses)  
            # Izsauc funkciju izdevuma pievienošanai

        elif choice == "2":  
            show_expenses(expenses)  
            # Izsauc funkciju izdevumu parādīšanai

        elif choice == "7":  
            print("Programma beidzas.")  
            # Parāda ziņu

            break  
            # Iziet no cikla un beidz programmu

        else:  
            print("Nepareiza izvēle.")  
            # Ja ievadīts nepareizs numurs


if __name__ == "__main__":  
    # Pārbauda vai fails tiek palaists tieši

    main()  
    # Palaiž galveno programmas funkciju