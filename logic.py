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