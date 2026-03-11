# Izdevumu izsekotājs (Expense Tracker)

## Projekta apraksts

Šis projekts ir vienkāršs Python komandrindas rīks, kas ļauj lietotājam reģistrēt un pārvaldīt ikdienas izdevumus. Programma ļauj pievienot jaunus izdevumus, skatīt izdevumu sarakstu, filtrēt tos pēc mēneša, aprēķināt kopsummas pa kategorijām, dzēst izdevumus un eksportēt datus CSV failā.

Programma saglabā visus izdevumus JSON failā, tāpēc dati tiek saglabāti arī pēc programmas aizvēršanas.

---

## Galvenās funkcijas

Programma nodrošina šādas funkcijas:

* Pievienot jaunu izdevumu
* Parādīt visus izdevumus tabulas formā
* Filtrēt izdevumus pēc mēneša
* Aprēķināt kopējo izdevumu summu
* Parādīt kopsavilkumu pa kategorijām
* Dzēst izdevumu pēc numura
* Eksportēt izdevumus CSV failā (atverams Excel)
* Saglabāt datus JSON failā

---

## Projekta struktūra

expense_tracker/

app.py – galvenā programma un lietotāja izvēlne
storage.py – datu saglabāšana un ielāde no JSON
logic.py – datu apstrādes funkcijas
export.py – CSV eksporta funkcija
expenses.json – datu fails (izveidojas automātiski)


DEVLOG.md – izstrādes žurnāls
plan.md – projekta sākotnējais plāns

README.md – projekta dokumentācija

---

## Kā palaist programmu

1. Pārliecinies, ka datorā ir instalēts Python.
2. Atver termināli projekta mapē.
3. Palaid programmu ar komandu:

python app.py

---

## Programmas izmantošana

Pēc programmas palaišanas terminālī parādās izvēlne.

1. Pievienot izdevumu
2. Parādīt izdevumus
3. Filtrēt pēc mēneša
4. Kopsavilkums pa kategorijām
5. Dzēst izdevumu
6. Eksportēt CSV
7. Iziet

Lietotājs ievada izvēles numuru un seko instrukcijām.

---

## Datu formāts

Izdevumi tiek saglabāti JSON failā šādā formātā:

[
{
"date": "2025-02-15",
"amount": 12.50,
"category": "Ēdiens",
"description": "Pusdienas kafejnīcā"
}
]

---

## Izmantotās Python bibliotēkas

json – darbam ar JSON failiem
csv – CSV eksporta funkcijai
os – failu eksistences pārbaudei
collections – kategoriju summēšanai

---

## Autors

Students: (Mārtiņš Kalninš)
Kurss: Python programmēšana
