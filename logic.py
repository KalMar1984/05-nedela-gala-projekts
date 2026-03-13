def sum_total(expenses):  
    # Funkcija aprēķina visu izdevumu kopējo summu

    total = 0  
    # Izveido mainīgo total un sākumā piešķir tam vērtību 0

    for e in expenses:  
        # Iet cauri katram izdevumam sarakstā
        amount = e.get("amount", 0)
        # Droša piekļuve summas laukam, ja lauks nav definēts, izmanto 0

        try:
            amount = float(amount)
            # Pārvērš summu par skaitli (ja tā bija teksts)
            total += amount
            # Pieskaita izdevuma summu kopējai summai tikai, ja tā ir skaitlis
        except (ValueError, TypeError):
            print(f"Brīdinājums: nederīga summa {amount} izdevumā {e}")
            # Ja summa nav skaitlis, parāda brīdinājumu

    return total  
    # Atgriež kopējo summu


def filter_by_month(expenses, year_month):
    # Funkcija filtrē izdevumus pēc konkrēta mēneša (piemēram "2025-02")

    filtered = []
    # Izveido tukšu sarakstu, kurā glabāsim tikai izvēlētā mēneša izdevumus

    for e in expenses:
        # Iet cauri katram izdevumam sarakstā
        date_str = str(e.get("date", "")).strip()
        # Droša piekļuve datuma laukam, ja nav, izmanto tukšu stringu

        if date_str.startswith(year_month):
            # Pārbauda vai izdevuma datums sākas ar izvēlēto gadu un mēnesi
            # piemēram "2025-02-15" sākas ar "2025-02"

            filtered.append(e)
            # Ja datums sakrīt, pievieno šo izdevumu filtrētajam sarakstam

    return filtered
    # Atgriež sarakstu ar atrastajiem izdevumiem


def sum_by_category(expenses):
    # Funkcija aprēķina kopējo summu katrai kategorijai

    result = {}
    # Izveido tukšu vārdnīcu (dictionary)
    # Tajā glabāsim kategoriju kā atslēgu un summu kā vērtību

    for e in expenses:
        # Iet cauri katram izdevumam
        cat = e.get("category", "Cits")
        # Droša piekļuve kategorijas laukam, ja nav, izmanto "Cits"
        amount = e.get("amount", 0)
        # Droša piekļuve summas laukam, ja nav, izmanto 0

        if cat not in result:
            # Pārbauda vai šāda kategorija jau eksistē vārdnīcā

            result[cat] = 0
            # Ja kategorijas vēl nav, izveido to ar sākuma summu 0

        try:
            amount = float(amount)
            # Pārvērš summu par skaitli (ja tā bija teksts)
            result[cat] += amount
            # Pieskaita izdevuma summu šai kategorijai tikai, ja tā ir skaitlis
        except (ValueError, TypeError):
            print(f"Brīdinājums: nederīga summa {amount} izdevumā {e}")
            # Ja summa nav skaitlis, parāda brīdinājumu

    return result
    # Atgriež vārdnīcu ar kategorijām un to summām


def get_available_months(expenses):
    # Funkcija atrod visus mēnešus, kuros ir izdevumi

    months = set()
    # Izveido set (īpašs saraksta veids bez dublikātiem)

    for e in expenses:
        # Iet cauri visiem izdevumiem
        date_str = str(e.get("date", "")).strip()
        # Droša piekļuve datuma laukam, ja nav, izmanto tukšu stringu

        if len(date_str) >= 7:
            month = date_str[:7]
            # Paņem tikai pirmās 7 rakstzīmes no datuma
            # piemēram "2025-02-15" → "2025-02"

            months.add(month)
            # Pievieno mēnesi set struktūrai

    months_list = list(months)
    # Pārvērš set par sarakstu

    months_list.sort()
    # Sakārto mēnešus augošā secībā

    return months_list
    # Atgriež sarakstu ar pieejamajiem mēnešiem