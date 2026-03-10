import csv  # Importē bibliotēku darbam ar CSV failiem


def export_csv(expenses, filename="expenses.csv"):  
    # Funkcija eksportē izdevumus CSV failā

    with open(filename, "w", newline="", encoding="utf-8") as f:  
        # Atver CSV failu rakstīšanas režīmā

        writer = csv.writer(f)  
        # Izveido CSV rakstītāja objektu

        writer.writerow(["Date", "Amount", "Category", "Description"])  
        # Ieraksta CSV faila pirmo rindu (kolonnu nosaukumus)

        for e in expenses:  # Iet cauri visiem izdevumiem
            writer.writerow([
                e["date"],         # Ieraksta datumu
                e["amount"],       # Ieraksta summu
                e["category"],     # Ieraksta kategoriju
                e["description"]   # Ieraksta aprakstu
            ])