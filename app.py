from export import export_to_csv  
# Importē funkciju kas eksportē izdevumus CSV failā

from storage import load_expenses, save_expenses  
# Importē funkcijas datu ielādei un saglabāšanai

from logic import sum_total, filter_by_month, sum_by_category, get_available_months  
# Importē funkciju kopējās summas aprēķināšanai un jaunās funkcijas filtrēšanai un kopsavilkumam

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

    # --- Droša kategorijas izvēle ---
    while True:
        # Cikls atkārtojas līdz lietotājs ievada pareizu kategorijas numuru
        try:
            cat_index = int(input("Izvēlies (1-7): ")) - 1
            # Lietotājs ievada kategorijas numuru
            if 0 <= cat_index < len(CATEGORIES):
                break
                # Pareiza ievade, cikls beidzas
            else:
                print("Nepareizs kategorijas numurs.")
                # Parāda kļūdas ziņu, ja numurs nav sarakstā
        except ValueError:
            print("Lūdzu ievadi skaitli.")
            # Parāda kļūdas ziņu, ja ievade nav skaitlis

    category = CATEGORIES[cat_index]
    # No saraksta paņem izvēlēto kategoriju

    # --- Droša summas ievade ---
    while True:
        try:
            amount = float(input("Summa (EUR): "))
            # Lietotājs ievada summu
            break
            # Pareiza ievade, cikls beidzas
        except ValueError:
            print("Summai jābūt skaitlim.")
            # Parāda kļūdas ziņu, ja ievade nav skaitlis

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


def filter_menu(expenses):
    # Funkcija ļauj lietotājam izvēlēties mēnesi un redzēt izdevumus

    months = get_available_months(expenses)
    # Izsauc funkciju kas atrod mēnešus ar izdevumiem

    if len(months) == 0:
        # Pārbauda vai mēnešu saraksts ir tukšs
        print("Nav neviena izdevuma.")
        # Ja nav izdevumu, parāda ziņu
        return
        # Beidz funkciju

    print("\nPieejamie mēneši:")
    # Izdrukā virsrakstu

    for i, m in enumerate(months, 1):
        # Iet cauri visiem mēnešiem un piešķir tiem numuru
        print(f"{i}) {m}")
        # Izdrukā mēnesi ar numuru

    # --- Droša mēneša izvēle ---
    try:
        choice = int(input("Izvēlies mēnesi: ")) - 1
        # Lietotājs ievada mēneša numuru
        if not (0 <= choice < len(months)):
            print("Nepareizs mēneša numurs.")
            return
            # Ja nepareizs numurs, beidz funkciju
    except ValueError:
        print("Lūdzu ievadi skaitli.")
        # Parāda kļūdas ziņu, ja ievade nav skaitlis
        return
        # Beidz funkciju

    selected_month = months[choice]
    # Saglabā izvēlēto mēnesi

    filtered = filter_by_month(expenses, selected_month)
    # Filtrē izdevumus pēc izvēlētā mēneša

    print(f"\n{selected_month} izdevumi:")
    # Izdrukā virsrakstu ar izvēlēto mēnesi

    for e in filtered:
        # Iet cauri visiem filtrētajiem izdevumiem
        print(f"{e['date']} | {e['amount']:6.2f} EUR | {e['category']:12} | {e['description']}")
        # Izdrukā vienu izdevuma rindu

    print("Kopā:", sum_total(filtered), "EUR")
    # Parāda kopējo summu izvēlētajam mēnesim


def category_summary(expenses):
    # Funkcija parāda kopsavilkumu pa kategorijām

    summary = sum_by_category(expenses)
    # Izsauc funkciju kas aprēķina summas pa kategorijām

    print("\nKopsavilkums pa kategorijām:")
    # Izdrukā virsrakstu

    total = 0
    # Mainīgais kopējai summai

    for cat, amount in summary.items():
        # Iet cauri vārdnīcai ar kategorijām un summām
        print(f"{cat:15} {amount:6.2f} EUR")
        # Izdrukā kategoriju un tās summu
        total += amount
        # Pieskaita summu kopējai summai

    print("----------------------------")
    # Izdrukā atdalīšanas līniju

    print("KOPĀ:", total, "EUR")
    # Parāda kopējo summu


def delete_expense(expenses):
    # Funkcija ļauj lietotājam dzēst izdevumu

    if len(expenses) == 0:
        # Pārbauda vai nav izdevumu
        print("Nav neviena izdevuma.")
        # Ja nav izdevumu, parāda ziņu
        return
        # Beidz funkciju

    print("\nIzdevumi:")
    # Izdrukā virsrakstu

    for i, e in enumerate(expenses, 1):
        # Iet cauri visiem izdevumiem un piešķir tiem numuru
        print(f"{i}) {e['date']} | {e['amount']:6.2f} EUR | {e['category']:12} | {e['description']}")
        # Izdrukā izdevumu sarakstu

    # --- Droša dzēšanas izvēle ---
    try:
        choice = int(input("\nKuru dzēst? (numurs vai 0 lai atceltu): "))
        # Lietotājs ievada izdevuma numuru
        if not (0 <= choice <= len(expenses)):
            print("Nepareizs numurs.")
            return
            # Ja nepareizs numurs, beidz funkciju
    except ValueError:
        print("Lūdzu ievadi skaitli.")
        # Parāda kļūdas ziņu, ja ievade nav skaitlis
        return
        # Beidz funkciju

    if choice == 0:
        # Ja lietotājs izvēlas 0
        return
        # Dzēšana tiek atcelta

    removed = expenses.pop(choice - 1)
    # Izņem izvēlēto izdevumu no saraksta

    save_expenses(expenses)
    # Saglabā izmaiņas JSON failā

    print(f"✓ Dzēsts: {removed['date']} | {removed['amount']} EUR | {removed['category']} | {removed['description']}")
    # Parāda ziņu ka izdevums dzēsts 


def export_menu(expenses):
    # Funkcija ļauj lietotājam eksportēt izdevumus CSV failā

    if len(expenses) == 0:
        # Pārbauda vai izdevumu saraksts ir tukšs
        print("Nav neviena izdevuma eksportēšanai.")
        # Ja nav izdevumu, parāda ziņu
        return
        # Beidz funkciju

    default_name = "izdevumi.csv"
    # Izveido mainīgo ar noklusējuma faila nosaukumu

    filename = input(f"Faila nosaukums [{default_name}]: ")
    # Lietotājam prasa ievadīt faila nosaukumu
    # Iekavās tiek parādīts noklusējuma nosaukums

    if filename == "":
        # Pārbauda vai lietotājs neko neievadīja
        filename = default_name
        # Ja tukšs, izmanto noklusējuma faila nosaukumu

    count = export_to_csv(expenses, filename)
    # Izsauc funkciju no export.py
    # Funkcija izveido CSV failu un atgriež eksportēto ierakstu skaitu

    print(f"✓ Eksportēts: {count} ieraksti -> {filename}")
    # Parāda paziņojumu cik ieraksti eksportēti un kāds ir faila nosaukums


def main():  
    # Galvenā programmas funkcija

    expenses = load_expenses()  
    # Ielādē izdevumus no JSON faila

    while True:  
        # Bezgalīgs cikls izvēlnei

        print("\n1) Pievienot izdevumu")  
        print("2) Parādīt izdevumus")
        print("3) Filtrēt pēc mēneša")
        print("4) Kopsavilkums pa kategorijām")
        print("5) Dzēst izdevumu")
        print("6) Eksportēt CSV")
        print("7) Iziet")

        choice = input("\nIzvēlies: ")  
        # Lietotājs ievada izvēles numuru

        if choice == "1":  
            add_expense(expenses)  

        elif choice == "2":  
            show_expenses(expenses)  

        elif choice == "3":
            filter_menu(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            export_menu(expenses)

        elif choice == "7":  
            print("Programma beidzas.")  
            break  

        else:  
            print("Nepareiza izvēle.")  


if __name__ == "__main__":  
    # Pārbauda vai fails tiek palaists tieši
    main()  
    # Palaiž galveno programmas funkciju main