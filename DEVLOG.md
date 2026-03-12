# DEVLOG
CLI Izdevumu pārvaldības programma (Expense Tracker)

Autors: Mārtiņš Kalninš
Kurss: Python programmēšana
Projekts: 05-nedela-gala-projekts  
Valoda: Python  
Tips: CLI (Command Line Interface) lietojumprogramma

---

# Projekta apraksts

Šis projekts ir vienkārša komandrindas (CLI) programma, kas ļauj lietotājam
pievienot, skatīt, filtrēt, analizēt un eksportēt personīgos izdevumus.

Programma ir veidota Python valodā un izmanto JSON failu datu saglabāšanai.
Tā tika izstrādāta kā kursa gala projekts ar mērķi praktiski pielietot:

- Python pamatus
- datu struktūras (list, dictionary)
- failu apstrādi
- moduļu struktūru
- Git versiju kontroli

---

# Arhitektūra

Projekts ir sadalīts vairākos failos:

app.py  
Galvenais programmas fails ar izvēlni un lietotāja mijiedarbību.

logic.py  
Funkcijas datu apstrādei (summas, filtrēšana, analīze).

storage.py  
Atbild par datu saglabāšanu un ielādi JSON failā.

export.py  
Eksportē izdevumus CSV failā.

expenses.json  
Fails, kur tiek saglabāti visi izdevumu ieraksti.

---

# Attīstības gaita

## 1. solis — Projekta pamats

Tika izveidota CLI programma ar pamata funkcijām:

- pievienot izdevumu
- parādīt visus izdevumus
- aprēķināt kopējo summu

Tika izveidoti pirmie moduļi:

app.py  
logic.py  
storage.py

Galvenais izaicinājums bija saprast,
kā sadalīt funkcionalitāti vairākos failos.

---

## 2. solis — Datu saglabāšana

Tika pievienota JSON datu glabāšana.

Funkcijas:

load_expenses()  
save_expenses()

Tagad programma saglabā visus izdevumus failā
un tie nepazūd pēc programmas aizvēršanas.

Tas bija svarīgs solis,
lai programma kļūtu par praktiski lietojamu rīku.

---

## 3. solis — Analīze un datu filtrēšana

Šajā solī tika pievienotas datu analīzes funkcijas:

filter_by_month()  
Filtrē izdevumus pēc mēneša.

sum_by_category()  
Aprēķina izdevumu summu katrai kategorijai.

get_available_months()  
Atrod mēnešus, kuros ir izdevumi.

Papildus tika izveidota funkcija:

delete_expense()

Kas ļauj lietotājam dzēst ierakstus no saraksta.

Šis solis būtiski uzlaboja programmas lietojamību.

---

## 4. solis — CSV eksports

Tika pievienota iespēja eksportēt izdevumus CSV failā.

Funkcija:

export_to_csv()

Tā ļauj saglabāt visus izdevumus tabulas formātā,
ko var atvērt Excel vai citā spreadsheet programmā.

Tas padara programmu noderīgu finanšu analīzei.

---

# Git izmantošana

Projekta izstrādes laikā tika izmantota Git versiju kontrole.

Galvenie soļi:

- repozitorija izveide GitHub
- commit katram projekta attīstības solim
- branch izmantošana funkciju izstrādei

Git palīdzēja sekot līdzi izmaiņām
un uzturēt projekta struktūru.

---

# Izaicinājumi

Galvenās problēmas projekta laikā:

1. Lietotāja ievades validācija
Nepareizi ievadīti dati var izraisīt programmas kļūdas.

2. Programmas struktūra
Sākumā bija grūti saprast,
kuras funkcijas kurā failā ievietot.

3. Git branch un commit pārvaldība

---

# Ko iemācījos

Šis projekts palīdzēja apgūt:

- Python funkcijas
- sarakstus un vārdnīcas
- failu saglabāšanu JSON
- CLI programmu izveidi
- moduļu struktūru
- Git un GitHub izmantošanu

---

# Iespējamie uzlabojumi nākotnē

- Grafiska lietotāja saskarne (GUI)
- Diagrammas izdevumu analīzei
- kategoriju rediģēšana
- datu filtrēšana pēc gada
- statistika pa mēnešiem
- SQLite datubāze

---

# Projekta statuss

Projekts ir funkcionāls CLI izdevumu pārvaldības rīks
ar pievienošanas, filtrēšanas, analīzes un eksporta iespējām.

Tas demonstrē Python pamatus un programmas strukturēšanu vairākos moduļos.