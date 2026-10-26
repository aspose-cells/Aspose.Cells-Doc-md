---
title: Aggiunta di campi di riga e colonna alla Tabella Pivot in Aspose.Cells for Python tramite Java
linktitle: Aggiunta di campi di riga e colonna alla Tabella Pivot
description: Scopri come aggiungere campi di base alle aree della riga e della colonna di una Tabella Pivot e controllare i subtotali dei campi della Tabella Pivot utilizzando PivotField.setSubtotals in Aspose.Cells for Python tramite Java.
keywords: Aspose.Cells, Python tramite Java, Tabella Pivot, campo di riga, campo di colonna, PivotField, setSubtotals, PivotFieldSubtotalType, subtotali
type: docs
weight: 220
url: /it/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aggiunta di un campo all'area della riga o della colonna**
Il metodo `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` sposta un campo di base dai dati di origine in una delle quattro aree della Tabella Pivot. L'argomento `fieldType` accetta uno dei seguenti valori dell'enumerazione `PivotFieldType`.
- `ROW` — campi visualizzati verticalmente a sinistra
- `COLUMN` — campi visualizzati orizzontalmente nella parte superiore
- `DATA` — campi i cui valori vengono aggregati
- `PAGE` — campi utilizzati come filtri del report
L'ordine di annidamento dei campi è importante. Aggiungendo prima `Category` all'area della riga e quindi `Item`, si ottiene una Tabella Pivot il cui raggruppamento esterno è `Category` e quello interno è `Item`. Invertendo l'ordine, si inverte anche la gerarchia.

## **Subtotali dei campi della Tabella Pivot**
Il metodo `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` controlla quali righe di subtotale vengono visualizzate per un campo della Tabella Pivot. Ogni chiamata attiva o disattiva in modo indipendente un singolo tipo di subtotale. Passando `shown = true`, il subtotale viene visualizzato, mentre passando `shown = false` viene nascosto. Poiché ogni chiamata influisce su un solo tipo, chiamare il metodo più volte con diversi valori `subtotalType` consente di creare un sottoinsieme personalizzato di subtotali.
L'enumerazione `PivotFieldSubtotalType` definisce i tipi di subtotale disponibili.
- `AUTOMATIC` — Aspose.Cells seleziona l'opzione predefinita (in genere `SUM` per i campi numerici)
- `NONE` — sopprime tutte le righe di subtotale
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
I subtotali vengono visualizzati solo se nell'area della riga o in quella della colonna sono presenti due o più campi della Tabella Pivot. Un singolo campo non presenta elementi significativi tra cui calcolare un subtotale; pertanto, le chiamate a `setSubtotals` non hanno effetti visibili in questo caso. Per questo motivo, in ogni esempio vengono inseriti due campi nell'area della riga (`Category` come campo esterno e `Item` come campo interno), in modo che sia visibile il confine del subtotale tra ciascun gruppo `Category`.
{{% /alert %}}

## **Scenario 1 — Subtotali automatici (predefiniti)**
Quando `setSubtotals` non viene chiamato, Aspose.Cells applica la selezione `AUTOMATIC` ai campi numerici. L'esempio seguente conferma esplicitamente questo comportamento chiamando `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` sul campo esterno `Category` dell'area della riga.

```python
import jpype
import asposecells
jpype.startJVM()
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
pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivotTable.calculateData()
workbook.save("output_automatic.xlsx")
jpype.shutdownJVM()
```

## **Scenario 2 — Soppressione di tutti i subtotali (NONE)**
La chiamata a `setSubtotals(PivotFieldSubtotalType.NONE, true)` rimuove tutte le righe di subtotale dalla Tabella Pivot, lasciando soltanto le righe dei campi e il totale generale nella parte inferiore. Questo è utile quando si desiderano i dati raggruppati grezzi senza alcuna riga riepilogativa.

```python
import jpype
import asposecells
jpype.startJVM()
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
pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, True)
pivotTable.calculateData()
workbook.save("output_none.xlsx")
jpype.shutdownJVM()
```

## **Scenario 3 — Sottoinsieme personalizzato di subtotali (SUM + AVERAGE)**
Non è possibile limitarsi a un singolo tipo di subtotale. Ogni chiamata a `setSubtotals` agisce su un singolo tipo in modo indipendente; chiamare il metodo due volte, una con `SUM` e una con `AVERAGE`, produce un sottoinsieme personalizzato di due righe di subtotale per ogni gruppo `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
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
pivotTable = pivotTables.add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, True)
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, True)
pivotTable.calculateData()
workbook.save("output_custom.xlsx")
jpype.shutdownJVM()
```

## **Riepilogo**
I tre scenari differiscono in un unico aspetto: le chiamate a `setSubtotals`. Tutto il resto — il set di dati, i campi e le aree a cui sono assegnati — è identico, il che rende i layout direttamente confrontabili.
- **Posizionamento dei campi.** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` sposta una colonna sorgente in una regione. All'interno di una stessa regione, l’ordine delle chiamate determina l’ordine di visualizzazione, per cui la prima chiamata corrisponde al gruppo più esterno. I subtotali richiedono due o più campi nella stessa regione: con un solo campo non vi è nulla tra i gruppi su cui calcolare il subtotale.
- **Scenario 1 — subtotali automatici.** Non chiamare `setSubtotals` lascia la scelta a Excel, che applica il proprio subtotale predefinito ai campi numerici. Chiamare `setSubtotals` con `PivotFieldSubtotalType.AUTOMATIC` registra esplicitamente tale scelta, invece di lasciarla implicita.
- **Scenario 2 — nessun subtotale.** `setSubtotals` con `PivotFieldSubtotalType.NONE` disattiva il subtotale predefinito, cosicché il pivot mantiene le righe del campo e il totale generale, ma non inserisce le righe di subtotale che Excel altrimenti inserirebbe tra di esse.
- **Scenario 3 — un sottoinsieme scelto.** Ogni chiamata attiva o disattiva esattamente un tipo di subtotale, e le chiamate si accumulano piuttosto che sovrascriveresi a vicenda. Pertanto, chiamare `setSubtotals` una volta con `PivotFieldSubtotalType.SUM` e una volta con `PivotFieldSubtotalType.AVERAGE` lascia entrambi abilitati, e il pivot genera un subtotale Somma, un subtotale Media e il totale generale.

{{% alert color="primary" %}}
Nulla riguardo i subtotali è specifico della regione delle righe. Le stesse chiamate a `setSubtotals` su un campo recuperato da `PivotTable.ColumnFields` producono gli stessi tre layout sull’asse delle colonne, poiché l’impostazione appartiene al campo pivot e non all’asse su cui esso è posizionato.
{{% /alert %}}

## **Articoli correlati**
- [Campi pagina nelle Tabelle Pivot](/cells/it/python-java/add-page-field-in-pivot-table/)
- [Aggiornamento delle Tabelle Pivot in Aspose.Cells for Python tramite Java](/cells/it/python-java/refresh-pivot-table/)
- [Applicazione di stili alle Tabelle Pivot](/cells/it/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}