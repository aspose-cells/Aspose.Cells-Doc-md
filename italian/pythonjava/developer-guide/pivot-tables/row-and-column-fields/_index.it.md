---
title: Row and Column Fields in Aspose.Cells for Python via Java
linktitle: Campi di riga e colonna
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /it/python-java/row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


I campi di riga e colonna sono gli elementi fondamentali di una tabella pivot. Un campo posizionato nella regione di riga appare verticalmente a sinistra della pivot, mentre un campo posizionato nella regione di colonna appare orizzontalmente nella parte superiore. Questo articolo mostra come aggiungere campi base a queste regioni in modo programmatico e come controllare i subtotali visualizzati tra i gruppi di campi utilizzando il metodo `PivotField.setSubtotals`.

## **Aggiungere un campo alla regione di riga o colonna**

Il metodo `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` sposta un campo base dai dati di origine in una delle quattro regioni della pivot. L'argomento `fieldType` accetta uno dei seguenti valori di `PivotFieldType`.

- `ROW` — campi posizionati verticalmente a sinistra
- `COLUMN` — campi posizionati orizzontalmente nella parte superiore
- `DATA` — campi i cui valori vengono aggregati
- `PAGE` — campi utilizzati come filtri del report

Dopo aver aggiunto i campi, è possibile accedervi tramite i metodi `PivotTable.getRowFields()` e `PivotTable.getColumnFields()`. Ogni metodo restituisce un `PivotFieldCollection`. Il campo all'indice 0 di `RowFields` è il campo di riga più esterno e gli indici successivi rappresentano i campi nidificati al suo interno. La stessa convenzione di indicizzazione si applica a `ColumnFields`.

L'ordine di nidificazione dei campi è importante. Aggiungendo prima `Category` alla regione di riga e poi `Item` si ottiene una pivot il cui raggruppamento esterno è `Category` e il cui raggruppamento interno è `Item`. Invertendo l'ordine si inverte la gerarchia.

## **Subtotali dei campi pivot**

Il metodo `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` controlla quali righe di subtotale vengono visualizzate per un campo pivot. Ogni chiamata attiva o disattiva un singolo tipo di subtotale in modo indipendente. Passando `shown = true` viene visualizzato il subtotale, mentre con `shown = false` viene nascosto. Poiché ogni chiamata influisce su un solo tipo, chiamare il metodo più volte con valori diversi di `subtotalType` consente di creare un sottoinsieme personalizzato di subtotali.

L'enum `PivotFieldSubtotalType` definisce i tipi di subtotale disponibili.

- `AUTOMATIC` — Aspose.Cells sceglie la selezione predefinita (in genere `SUM` per i campi numerici)
- `NONE` — elimina ogni riga di subtotale
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
I subtotali vengono visualizzati solo quando ci sono due o più campi pivot nella regione di riga (o nella regione di colonna). Un singolo campo non ha nulla di significativo da subtotalizzare, quindi le chiamate a `setSubtotals` non hanno alcun effetto visibile in quel caso. Questo articolo quindi posiziona due campi di riga (`Category` esterno, `Item` interno) in ogni esempio, in modo che il confine del subtotale tra ciascun gruppo `Category` sia visibile.
{{% /alert %}}

## **Scenario 1 — Subtotali automatici (predefiniti)**

Quando non si chiama affatto `setSubtotals`, Aspose.Cells applica la selezione `AUTOMATIC` ai campi numerici. L'esempio seguente conferma esplicitamente questo comportamento chiamando `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` sul campo di riga esterno `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, PivotTable, PivotField, PivotFieldType, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

worksheet.getCells().get(0, 0).putValue("Category")
worksheet.getCells().get(0, 1).putValue("Item")
worksheet.getCells().get(0, 2).putValue("Year")
worksheet.getCells().get(0, 3).putValue("Amount")

worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)

worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)

worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)

worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)

worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)

worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)

worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)

worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)

pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output_automatic.xlsx")

jpype.shutdownJVM()
```

## **Scenario 2 — Eliminare tutti i subtotali (None)**

Chiamando `setSubtotals(PivotFieldSubtotalType.NONE, true)` si rimuove ogni riga di subtotale dalla pivot, lasciando solo le righe dei campi e il totale generale in fondo. Ciò è utile quando si desiderano i dati raggruppati grezzi senza righe di riepilogo.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.getCells().get(0, j).putValue(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80 ],
    ["Fruit",     "Banana", 2021, 90 ],
    ["Vegetable", "Carrot", 2020, 50 ],
    ["Vegetable", "Carrot", 2021, 60 ],
    ["Vegetable", "Daikon", 2020, 40 ],
    ["Vegetable", "Daikon", 2021, 45 ]
]

for i in range(len(data)):
    for j in range(len(data[0])):
        worksheet.getCells().get(i + 1, j).putValue(data[i][j])

pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, True)
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output_none.xlsx")

jpype.shutdownJVM()
```

## **Scenario 3 — Sottoinsieme di subtotali personalizzato (Sum + Average)**

Non si è limitati a un singolo tipo di subtotale. Ogni chiamata a `setSubtotals` opera in modo indipendente su un tipo, quindi chiamando il metodo due volte — una con `SUM` e una con `AVERAGE` — si produce un sottoinsieme personalizzato di due righe di subtotale per ciascun gruppo `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableCollection, PivotTable, PivotFieldType, PivotField, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

worksheet.getCells().get("A1").putValue("Category")
worksheet.getCells().get("B1").putValue("Item")
worksheet.getCells().get("C1").putValue("Year")
worksheet.getCells().get("D1").putValue("Amount")

worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)

worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)

worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)

worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)

worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)

worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)

worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)

worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)

pivotTables = worksheet.getPivotTables()
pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Category")
pivotTable.addFieldToArea(PivotFieldType.Row, "Item")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.Sum, True)
categoryField.setSubtotals(PivotFieldSubtotalType.Average, True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output_custom.xlsx")

jpype.shutdownJVM()
## **Riepilogo**

I tre scenari precedenti condividono lo stesso set di dati e la stessa struttura di tabella pivot. L'unica differenza tra essi è la chiamata a `setSubtotals` applicata al campo di riga esterno `Category`. Ricorda la regola dei due campi: un singolo campo in una regione non ha nulla da subtotalizzare, quindi posiziona sempre almeno due campi nella regione di riga o colonna quando desideri che `setSubtotals` abbia un effetto visibile.

## **Articoli correlati**

- [Campi pagina nelle tabelle pivot](/cells/it/python-java/add-page-field-in-pivot-table/)
- [Aggiornamento delle tabelle pivot in Aspose.Cells for Python via Java](/cells/it/python-java/refresh-pivot-table/)
- [Applicazione di stili alle tabelle pivot](/cells/it/python-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
