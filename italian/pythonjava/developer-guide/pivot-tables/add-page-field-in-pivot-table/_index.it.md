---
title: Aggiungere campi filtro a una tabella pivot in Aspose.Cells per .NET
linktitle: Aggiungere campi filtro
description: Scopri come aggiungere e configurare i campi filtro nelle tabelle pivot utilizzando Aspose.Cells for Python via Java, inclusi l'aggiunta di campi filtro, il filtraggio a selezione singola e il filtraggio multi-selezione.
keywords: Aspose.Cells, Python, Java, tabella pivot, campo filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /it/python-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'intero ciclo di vita dei campi filtro nelle tabelle pivot. È possibile aggiungere un campo filtro tramite un'API di alto livello comoda da usare oppure tramite la raccolta di livello inferiore `page_fields`, e si può gestire il filtro pagina in modalità selezione singola, azzerarlo per mostrare ogni elemento della pagina, oppure commutare il campo in multi-selezione così che gli utenti possano scegliere più elementi di pagina contemporaneamente tramite l'interfaccia a caselle di controllo in Excel.
{{% /alert %}}

## **Introduzione**

Un campo filtro è un campo pivot che controlla *quale sottoinsieme* dei dati di origine viene visualizzato nel corpo della tabella pivot. Gli utenti finali lo vedono come un menu a discesa nella parte superiore di una tabella pivot renderizzata in Excel, e selezionare uno degli elementi di pagina disponibili ricostruisce il corpo della tabella pivot in modo che vengano riepilogati solo i record appartenenti a quell'elemento di pagina. Un campo pivot diventa un campo filtro quando viene registrato come `PivotFieldType.PAGE` anziché `PivotFieldType.ROW`, `PivotFieldType.COLUMN` o `PivotFieldType.DATA`.

Un campo filtro può operare in due modalità. Nella modalità predefinita **selezione singola** è visibile un solo elemento di pagina alla volta, quindi il corpo della tabella pivot riepiloga esattamente un sottoinsieme. Nella modalità **multi-selezione** il campo espone un elenco di caselle di controllo e il corpo della tabella pivot riepiloga l'unione di ogni elemento di pagina selezionato. Lo stesso campo di origine può essere spostato avanti e indietro tra queste modalità attivando o disattivando una singola proprietà.

Aspose.Cells for Python via Java espone due modi equivalenti per registrare un campo filtro. L'API di alto livello è `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")`, che riceve il nome della colonna di origine e aggiunge il campo in una sola chiamata. L'API di livello inferiore è `PivotTable.page_fields.add(PivotField)`, che si utilizza quando si dispone già di un riferimento a `PivotField` e si desidera aggiungere la stessa istanza del campo all'area filtro. Entrambe le API finiscono per popolare la stessa raccolta `page_fields`, e il resto di questo articolo mostra come scegliere tra di esse e come gestire ciascuna modalità di filtraggio.

## **Aggiungere un campo filtro**

Esistono due modi per registrare un campo pivot nell'area filtro. La chiamata di alto livello riceve il nome della colonna di origine come stringa ed è il percorso più comune. La chiamata di livello inferiore accetta un'istanza esistente di `PivotField` ed è comoda quando lo stesso oggetto campo deve essere riutilizzato in più aree della tabella pivot. Entrambe le chiamate collocano il campo in `PivotTable.page_fields`, dopodiché appare come menu a discesa della pagina nella parte superiore della tabella pivot renderizzata.

### Aggiungere un campo filtro con add_field_to_area

L'esempio seguente crea un piccolo dataset Fruit / Year / Amount, posiziona una tabella pivot alla cella E3 con `Fruit` nell'area righe, `Amount` nell'area dati e `Year` nell'area filtro, aggiorna la tabella pivot e salva la cartella di lavoro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType

# Crea una nuova cartella di lavoro
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

# Imposta la riga di intestazione
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Popola 9 righe di dati di esempio: Frutta, Anno, Quantità
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
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])

# Aggiungi una tabella pivot ancorata alla cella E3
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Aggiungi campi alle loro aree: Frutta come Riga, Quantità come Dati, Anno come Campo Pagina
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Aggiorna e calcola i dati della tabella pivot
pivotTable.refreshData()
pivotTable.calculateData()

# Salva la cartella di lavoro
workbook.save("pageFieldSample.xlsx")

jpype.shutdownJVM()
```

### Aggiungere un campo filtro con page_fields.add

Quando si lavora già con un'istanza di `PivotField`, è possibile passarla direttamente a `PivotTable.page_fields.add`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale nell'area filtro viene sostituita con la chiamata all'API di livello inferiore.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType

# — La tabella pivot e il campo pagina sono costruiti esattamente come in
#   Scenario 1a (dati Frutto/Anno/Importo, pivot in E3, Frutto→Riga,
#   Importo→Dati). Di seguito otteniamo il PivotField Anno dalla
#   collezione BaseFields e lo passiamo a PageFields.Add — l'
#   alternativa di basso livello a AddFieldToArea. Il risultato è
#   funzionalmente identico allo Scenario 1a.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Intestazioni
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

# Dati di esempio (9 righe)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)

# Aggiungi tabella pivot in E3 coprendo A1:C10
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Frutto -> Riga, Importo -> Dati (Anno andrà nella Pagina sotto)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Approccio di basso livello: prendi il PivotField Anno esistente da BaseFields
# e registralo nell'area Pagina tramite PageFields.Add(PivotField).
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)

# Aggiorna così che il nuovo campo pagina venga riflesso nel workbook salvato
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Filtraggio a selezione singola (mostrare un elemento di pagina)**

Nel comportamento predefinito a selezione singola, il campo filtro viene reso come un singolo menu a discesa e l'intero `PivotField.current_page_item` seleziona quale elemento di pagina guida il corpo della tabella pivot. Assegnando un indice specifico si seleziona quell'unico elemento; assegnando il valore sentinella speciale `0x7FFD` (decimale 32765) si azzera il filtro così che ogni elemento di pagina venga riepilogato contemporaneamente. La selezione singola è il valore predefinito; non è necessario abilitarla esplicitamente.

### Mostrare tutti gli elementi

Impostare `current_page_item` sul valore magico `0x7FFD` equivale ad azzerare il filtro pagina: il corpo della tabella pivot riepiloga ogni elemento di pagina come se non fosse applicato alcun filtro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crea una nuova cartella di lavoro
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Popola i dati Frutto/Anno/Importo
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

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
        sheet.getCells().get(r + 1, c).putValue(data[r][c])

# Crea tabella pivot in E3
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)

# Configura i campi pivot: Frutto→Riga, Importo→Dati, Anno→Pagina
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")

pivotTable.refreshData()
pivotTable.calculateData()

# Cancella il filtro pagina così ogni elemento nel campo pagina è visibile.
# 0x7FFD (decimale 32765) è il valore sentinella speciale che significa "tutti gli elementi" —
# equivalente a selezionare "(Tutti)" nel menu a discesa del campo pagina di Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Mostrare un elemento specifico

Impostare `current_page_item` su un indice reale seleziona solo quell'elemento di pagina. L'indice è la posizione dell'elemento nell'elenco ordinato degli elementi del campo filtro, quindi ad esempio `1` seleziona il secondo elemento dopo l'ordinamento.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crea il workbook
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Aggiungi dati di esempio (Frutto/Anno/Importo)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")

cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")

cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")

cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")

cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")

# Aggiungi tabella pivot in E3
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Aggiungi campi: Frutto→Riga, Importo→Dati, Anno→Pagina
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Operazioni specifiche del campo pagina
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = secondo elemento nell'ordine ordinato (es. "2021")

# Aggiorna e calcola la tabella pivot
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Filtraggio multi-selezione**

Il filtraggio multi-selezione trasforma il menu a discesa della pagina in un elenco di caselle di controllo e consente all'utente finale di selezionare più elementi di pagina contemporaneamente. Aspose.Cells espone due proprietà che lavorano insieme. `PivotField.is_multiple_item_selection_allowed` deve essere impostato su `True` prima che l'interfaccia multi-selezione abbia effetto. Dopo averla abilitata, `PivotItem.is_hidden` controlla quali elementi appaiono nell'elenco delle caselle di controllo, così è possibile mostrare ogni elemento o autorizzare solo elementi specifici.

Il codice seguente abilita la multi-selezione sullo stesso campo filtro Year costruito nello Scenario 1a, e quindi mostra due pattern: la Parte A rivela ogni elemento di pagina lasciando `is_hidden` impostato su `False` per ogni voce, mentre la Parte B autorizza solo i valori di origine scelti e nasconde tutto il resto tramite un blocco `switch (pivot_items[i].get_string_value())`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — La tabella pivot e il campo pagina sono costruiti esattamente come in
#   Scenario 1a (dati Frutto/Anno/Importo, pivot in E3, Frutto→Riga,
#   Importo→Dati, Anno→Pagina tramite AddFieldToArea).
#   Di seguito applichiamo il filtro multi-selezione sul campo pagina.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Dati di esempio: Frutto | Anno | Importo
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")

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
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))

pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# — Abilita la multi-selezione sul campo pagina
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# Parte A — seleziona TUTTI gli elementi (rendi visibile ogni elemento)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# Parte B — seleziona solo elementi specifici per valore di origine
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

> **Nota:** Quando si utilizza il filtraggio multi-selezione tramite `PivotItem.is_hidden`, **almeno un `PivotItem` deve rimanere visibile** (`is_hidden == False`). Se ogni elemento è nascosto, Excel si arresta in modo anomalo all'apertura del file oppure rende una tabella pivot vuota. Verificare sempre che la whitelist di multi-selezione includa almeno un elemento dei dati di origine.

## **Quale API e quale modalità devo usare?**

La tabella seguente riassume quando utilizzare ciascuna API e modalità così da poter scegliere la combinazione corretta senza leggere ogni scenario nel dettaglio.

| Scenario / Caso d'uso | API consigliata | Proprietà utilizzata | Note |
|---|---|---|---|
| Aggiungere un campo filtro tramite il nome della colonna di origine (caso più comune) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | n/d | Alto livello, una sola riga. Usare questa opzione a meno che non serva un riferimento a `PivotField`. |
| Aggiungere un campo filtro quando si ha già un oggetto `PivotField` | `PivotTable.page_fields.add(PivotField)` | n/d | Usare quando l'oggetto campo è stato ottenuto altrove o deve essere riutilizzato. |
| Filtrare un singolo elemento di pagina (modalità predefinita) | `PivotField.current_page_item` | impostare su un indice specifico | Ad esempio, `1` mostra il secondo elemento nell'elenco ordinato. |
| Mostrare tutti gli elementi / azzerare il filtro pagina | `PivotField.current_page_item` | impostare su `0x7FFD` | Il valore magico `0x7FFD` (decimale 32765) è la sentinella per "tutti gli elementi". |
| Abilitare l'interfaccia multi-selezione in Excel | `PivotField.is_multiple_item_selection_allowed` | impostare su `True` | Richiesto prima che qualsiasi chiamata a `is_hidden` abbia effetto. |
| Nascondere / mostrare singoli elementi in un elenco multi-selezione | `PivotItem.is_hidden` | impostare per ciascun elemento | Almeno un elemento deve rimanere visibile (`is_hidden == False`). |

{{% alert color="primary" %}}
Ricordare sempre il vincolo di visibilità quando si configura il filtraggio multi-selezione. Se ogni `PivotItem` in un campo filtro multi-selezione è nascosto, Excel si arresta in modo anomalo all'apertura oppure rende una tabella pivot vuota. Costruire la whitelist sui dati di origine in modo che almeno un elemento rimanga visibile e le cartelle di lavoro salvate si apriranno in modo affidabile su ogni macchina.
{{% /alert %}}



{{< app/cells/assistant language="python" >}}