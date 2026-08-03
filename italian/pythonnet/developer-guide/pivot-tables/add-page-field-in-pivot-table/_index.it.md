---
title: Aggiungere campi filtro a una tabella pivot in Aspose.Cells per .NET
linktitle: Aggiungere campi filtro
description: Scopri come aggiungere e configurare i campi filtro nelle tabelle pivot utilizzando Aspose.Cells for Python via .NET, inclusi aggiunta di campi filtro, filtro a selezione singola e filtro a selezione multipla.
keywords: Aspose.Cells, Python via .NET, tabella pivot, campo filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /it/python-net/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'intero ciclo di vita dei campi filtro nelle tabelle pivot. È possibile aggiungere un campo filtro tramite un'API di alto livello o tramite la raccolta di basso livello `page_fields`, e si può gestire il filtro della pagina in modalità selezione singola, cancellarlo per mostrare ogni elemento della pagina, oppure commutare il campo alla selezione multipla così che gli utenti possano scegliere più elementi della pagina contemporaneamente tramite l'interfaccia delle caselle di controllo in Excel.
{{% /alert %}}

## **Introduzione**

Un campo filtro è un campo pivot che controlla *quale sottoinsieme* dei dati di origine viene visualizzato nel corpo della tabella pivot. Gli utenti finali lo vedono come un menu a discesa nella parte superiore di una tabella pivot renderizzata in Excel, e selezionare uno degli elementi della pagina disponibili ricostruisce il corpo della tabella pivot in modo che vengano riepilogati solo i record appartenenti a quell'elemento della pagina. Un campo pivot diventa un campo filtro quando viene registrato come `PivotFieldType.PAGE` invece di `PivotFieldType.ROW`, `PivotFieldType.COLUMN` o `PivotFieldType.DATA`.

Un campo filtro può operare in due comportamenti. Nel comportamento predefinito di **selezione singola** solo un elemento della pagina è visibile alla volta, quindi il corpo della tabella pivot riepiloga esattamente un sottoinsieme. Nel comportamento di **selezione multipla** il campo espone un elenco di caselle di controllo, e il corpo della tabella pivot riepiloga l'unione di ogni elemento della pagina selezionato. Lo stesso campo di origine può essere spostato avanti e indietro tra questi comportamenti attivando/disattivando una singola proprietà.

Aspose.Cells for Python via .NET espone due modi equivalenti per registrare un campo filtro. L'API di alto livello è `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")`, che accetta il nome della colonna di origine e aggiunge il campo in una singola chiamata. L'API di basso livello è `PivotTable.page_fields.add(PivotField)`, che viene utilizzata quando si possiede già un riferimento `PivotField` e si desidera aggiungere la stessa istanza di campo all'area della pagina. Entrambe le API finiscono per popolare la stessa raccolta `page_fields`, e il resto di questo articolo dimostra come scegliere tra esse e come gestire ciascuna modalità di filtro.

## **Aggiungere un campo filtro**

Ci sono due modi per registrare un campo pivot nell'area della pagina. La chiamata di alto livello accetta il nome della colonna di origine come stringa ed è il percorso più comune. La chiamata di basso livello accetta un'istanza esistente di `PivotField` ed è comoda quando lo stesso oggetto campo deve essere riutilizzato tra più aree della tabella pivot. Entrambe le chiamate collocano il campo in `PivotTable.page_fields`, dopodiché appare come menu a discesa della pagina nella parte superiore della tabella pivot renderizzata.

### Aggiungere un campo filtro con add_field_to_area

L'esempio seguente crea un piccolo set di dati Frutta / Anno / Importo, posiziona una tabella pivot nella cella E3 con `Fruit` nell'area delle righe, `Amount` nell'area dei dati e `Year` nell'area della pagina, aggiorna la tabella pivot e salva la cartella di lavoro.

```python
import aspose.cells as ac

# Crea una nuova cartella di lavoro
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Imposta la riga di intestazione
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Popola 9 righe di dati di esempio: Frutto, Anno, Quantità
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])

# Aggiungi una tabella pivot ancorata alla cella E3
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Aggiungi i campi alle rispettive aree: Frutto come Riga, Quantità come Dati, Anno come campo Pagina
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

# Aggiorna e calcola i dati della tabella pivot
pivot_table.calculate_data()

# Salva la cartella di lavoro
workbook.save("pageFieldSample.xlsx")
```

### Aggiungere un campo filtro con page_fields.add

Quando si lavora già con un'istanza di `PivotField`, è possibile passarla direttamente a `PivotTable.page_fields.add`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale nell'area della pagina viene sostituita con la chiamata all'API di basso livello.

```python
import aspose.cells as ac

# — La tabella pivot e il campo pagina sono costruiti esattamente come in
#   Scenario 1a (dati Fruit/Year/Amount, pivot in E3, Fruit→Riga,
#   Amount→Dati). Di seguito otteniamo il PivotField Year dalla
#   raccolta BaseFields e lo passiamo a PageFields.Add — l'
#   alternativa a basso livello a AddFieldToArea. Il risultato è
#   funzionalmente identico allo Scenario 1a.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Intestazioni
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

# Dati di esempio (9 righe)
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)

# Aggiungi tabella pivot in E3 coprendo A1:C10
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]

# Fruit -> Riga, Amount -> Dati (Year andrà in Page qui sotto)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Approccio a basso livello: prendi il PivotField Year esistente da BaseFields
# e registralo nell'area Page tramite PageFields.Add(PivotField).
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)

# Aggiorna affinché il nuovo campo pagina venga riflesso nella cartella di lavoro salvata
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Filtro a selezione singola (Mostrare un elemento della pagina)**

Nel comportamento predefinito di selezione singola, il campo filtro viene renderizzato come un singolo menu a discesa e l'intero `PivotField.current_page_item` seleziona quale elemento della pagina guida il corpo della tabella pivot. Assegnare un indice specifico seleziona quell'unico elemento; assegnare il valore sentinella speciale `0x7FFD` (decimale 32765) cancella il filtro così che ogni elemento della pagina venga riepilogato contemporaneamente. La selezione singola è il valore predefinito; non è necessario abilitarla esplicitamente.

### Mostrare tutti gli elementi

Impostare `current_page_item` al valore magico `0x7FFD` equivale a cancellare il filtro della pagina: il corpo della tabella pivot riepiloga ogni elemento della pagina come se non fosse applicato alcun filtro.

```python
import aspose.cells as ac

# Crea una nuova cartella di lavoro
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Popola i dati Frutto/Anno/Importo
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.cells[r + 1, c].put_value(data[r][c])

# Crea una tabella pivot in E3
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]

# Configura i campi pivot: Frutto→Riga, Importo→Dati, Anno→Pagina
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

pivot_table.calculate_data()

# Cancella il filtro pagina in modo che ogni elemento nel campo pagina sia visibile.
# 0x7FFD (decimale 32765) è il valore sentinella speciale che significa "tutti gli elementi" —
# equivalente a selezionare "(Tutti)" nel menu a discesa del campo pagina di Excel.
pivot_table.page_fields[0].current_page_item = 0x7FFD

workbook.save("output.xlsx")
```

### Mostrare un elemento specifico

Impostare `current_page_item` su un indice reale seleziona solo quell'unico elemento della pagina. L'indice è la posizione dell'elemento nell'elenco ordinato degli elementi del campo filtro, quindi ad esempio `1` seleziona il secondo elemento dopo l'ordinamento.

```python
import aspose.cells as ac

# Crea cartella di lavoro
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Aggiungi dati di esempio (Frutta/Anno/Importo)
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")

cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")

cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")

cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")

cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")

# Aggiungi tabella pivot in E3
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Aggiungi campi: Frutta→Riga, Importo→Dati, Anno→Pagina
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# Operazioni specifiche del campo pagina
pivot_table.page_fields[0].current_page_item = 1  # 1 = secondo elemento nell'ordine ordinato (es. "2021")

# Aggiorna e calcola la tabella pivot
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Filtro a selezione multipla**

Il filtro a selezione multipla trasforma il menu a discesa della pagina in un elenco di caselle di controllo e consente all'utente finale di selezionare più elementi della pagina contemporaneamente. Aspose.Cells espone due proprietà che lavorano insieme. `PivotField.is_multiple_item_selection_allowed` deve essere impostato su `True` prima che l'interfaccia di selezione multipla abbia effetto. Dopo che è abilitata, `PivotItem.is_hidden` controlla quali elementi appaiono nell'elenco delle caselle di controllo, quindi è possibile mostrare ogni elemento o autorizzare solo elementi specifici.

Il codice seguente abilita la selezione multipla sullo stesso campo filtro Year costruito nello Scenario 1a, e quindi mostra due pattern: la Parte A rivela ogni elemento della pagina lasciando `is_hidden` impostato su `False` per ogni voce, mentre la Parte B autorizza solo i valori di origine scelti e nasconde tutto il resto tramite un blocco `if` / `elif` che verifica `pivot_items[i].get_string_value()`.

```python
import aspose.cells as ac

# — La tabella pivot e il campo pagina sono costruiti esattamente come nello
#   Scenario 1a (dati Fruit/Year/Amount, pivot in E3, Fruit→Riga,
#   Amount→Dati, Year→Pagina tramite AddFieldToArea).
#   Di seguito applichiamo il filtro multi-selezione sul campo pagina.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Dati di esempio: Fruit | Year | Amount
cells[0, 0].put_value("Fruit")
cells[0, 1].put_value("Year")
cells[0, 2].put_value("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells[i + 1, 0].put_value(data[i][0])
    cells[i + 1, 1].put_value(int(data[i][1]))
    cells[i + 1, 2].put_value(int(data[i][2]))

pivot_sheet = workbook.worksheets.add("Pivot")
pivots = pivot_sheet.pivot_tables
pivot_index = pivots.add("E3", "A1:C10", "PivotTable1")
pivot_table = pivots[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# — Abilita la multi-selezione sul campo pagina
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True

# Parte A — seleziona TUTTI gli elementi (rendi visibile ogni elemento)
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False

# Parte B — seleziona solo elementi specifici per valore di origine
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True

pivot_table.calculate_data()

workbook.save("output.xlsx")
```

> **Nota:** Quando si utilizza il filtro a selezione multipla tramite `PivotItem.is_hidden`, **almeno un `PivotItem` deve rimanere visibile** (`is_hidden == False`). Se ogni elemento è nascosto, Excel si blocca all'apertura del file oppure rende una tabella pivot vuota. Verificare sempre che l'elenco degli elementi consentiti per la selezione multipla includa almeno un elemento dai dati di origine.

## **Quale API e quale modalità dovrei usare?**

La tabella seguente riassume quando utilizzare ciascuna API e modalità, così da poter scegliere la combinazione giusta senza leggere ogni scenario nel dettaglio.

| Scenario / Caso d'uso | API consigliata | Proprietà utilizzata | Note |
|---|---|---|---|
| Aggiungere un campo filtro tramite il nome della colonna di origine (caso più comune) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | n/a | Alto livello, una sola riga. Utilizzare questo a meno che non serva un riferimento `PivotField`. |
| Aggiungere un campo filtro quando si ha già un oggetto `PivotField` | `PivotTable.page_fields.add(PivotField)` | n/a | Utilizzare quando l'oggetto campo è stato ottenuto altrove o deve essere riutilizzato. |
| Filtrare un singolo elemento della pagina (modalità predefinita) | `PivotField.current_page_item` | impostare su un indice specifico | Ad esempio, `1` mostra il secondo elemento nell'elenco ordinato. |
| Mostrare tutti gli elementi / cancellare il filtro della pagina | `PivotField.current_page_item` | impostare su `0x7FFD` | Il valore magico `0x7FFD` (decimale 32765) è il valore sentinella per "tutti gli elementi". |
| Abilitare l'interfaccia di selezione multipla in Excel | `PivotField.is_multiple_item_selection_allowed` | impostare su `True` | Richiesto prima che qualsiasi chiamata a `is_hidden` abbia effetto. |
| Nascondere / mostrare singoli elementi in un elenco a selezione multipla | `PivotItem.is_hidden` | impostare per ogni elemento | Almeno un elemento deve rimanere visibile (`is_hidden == False`). |

{{% alert color="primary" %}}
Ricordare sempre il vincolo di visibilità quando si configura il filtro a selezione multipla. Se ogni `PivotItem` in un campo filtro a selezione multipla è nascosto, Excel si blocca all'apertura o rende una tabella pivot vuota. Costruire l'elenco degli elementi consentiti in base ai dati di origine in modo che almeno un elemento rimanga visibile, e le cartelle di lavoro salvate si apriranno in modo affidabile su ogni macchina.
{{% /alert %}}

{{< app/cells/assistant language="python-net" >}}
