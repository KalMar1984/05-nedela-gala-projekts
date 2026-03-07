import json  # Importē bibliotēku darbam ar JSON failiem
import os    # Importē bibliotēku darbam ar failu sistēmu

FILE_NAME = "expenses.json"  # Faila nosaukums, kurā saglabāsim izdevumus


def load_expenses():  # Funkcija, kas ielādē izdevumus no JSON faila
    if not os.path.exists(FILE_NAME):  # Pārbauda vai fails eksistē
        return []  # Ja fails neeksistē, atgriež tukšu sarakstu

    with open(FILE_NAME, "r", encoding="utf-8") as f:  # Atver failu lasīšanas režīmā
        return json.load(f)  # Nolasa JSON failu un pārvērš to Python sarakstā


def save_expenses(expenses):  # Funkcija, kas saglabā izdevumus JSON failā
    with open(FILE_NAME, "w", encoding="utf-8") as f:  # Atver failu rakstīšanas režīmā
        json.dump(expenses, f, indent=2, ensure_ascii=False)  
        # json.dump saglabā Python sarakstu JSON failā
        # indent=2 padara failu lasāmāku
        # ensure_ascii=False ļauj saglabāt latviešu burtus