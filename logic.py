def sum_total(expenses):  
    # Funkcija aprēķina visu izdevumu kopējo summu

    total = 0  
    # Izveido mainīgo total un sākumā piešķir tam vērtību 0

    for e in expenses:  
        # Iet cauri katram izdevumam sarakstā

        total += e["amount"]  
        # Pieskaita izdevuma summu kopējai summai

    return total  
    # Atgriež kopējo summu 

    def filter_by_month(expenses, year_month):
    # Funkcija filtrē izdevumus pēc konkrēta mēneša (piemēram "2025-02")

    filtered = []
    # Izveido tukšu sarakstu, kurā glabāsim tikai izvēlētā mēneša izdevumus

    for e in expenses:
        # Iet cauri katram izdevumam sarakstā

        if e["date"].startswith(year_month):
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

        cat = e["category"]
        # Saglabā izdevuma kategoriju mainīgajā

        if cat not in result:
            # Pārbauda vai šāda kategorija jau eksistē vārdnīcā

            result[cat] = 0
            # Ja kategorijas vēl nav, izveido to ar sākuma summu 0

        result[cat] += e["amount"]
        # Pieskaita izdevuma summu šai kategorijai

    return result
    # Atgriež vārdnīcu ar kategorijām un to summām


def get_available_months(expenses):
    # Funkcija atrod visus mēnešus, kuros ir izdevumi

    months = set()
    # Izveido set (īpašs saraksta veids bez dublikātiem)

    for e in expenses:
        # Iet cauri visiem izdevumiem

        month = e["date"][:7]
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