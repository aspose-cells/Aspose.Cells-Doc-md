---
title: Campi Valore in Aspose.Cells for Python via Java
linktitle: Campi Valore
description: Scopri come aggiungere campi base all'area dati di una tabella pivot, modificare la funzione di riepilogo con PivotField.Function e visualizzare il campo valore sull'asse Riga o Colonna in Aspose.Cells for Python via Java
keywords: Aspose.Cells, Python via Java, tabella pivot, campo valore, PivotField, PivotField.Function, campo dati, PivotTable.ValuesField, Somma, Media
type: docs
weight: 230
url: /it/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Aggiunta di un Campo all'Area Dati

L'aggiunta di un campo base all'area dati (valore) è il primo passo per definire come una tabella pivot aggrega i dati di origine. Aspose.Cells espone `PivotTable.addFieldToArea(PivotFieldType, string)`, un overload che accetta la costante `PivotFieldType.DATA` e il nome della colonna di origine. Una volta che un campo viene aggiunto all'area dati, l'API lo espone attraverso la raccolta `PivotTable.DataFields`, nell'ordine in cui i campi sono stati aggiunti. Per impostazione predefinita, una colonna di origine numerica viene riassunta con `ConsolidationFunction.SUM`, mentre una colonna non numerica utilizza `COUNT` come valore predefinito.

## Modifica della Funzione di Riepilogo

Ogni campo posizionato nell'area dati viene incapsulato internamente come un'istanza di `PivotField`, e la sua proprietà `Function` restituisce un valore dall'enum `ConsolidationFunction`. Lo stesso setter `Function` consente di passare tra gli aggregati disponibili, tra cui `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STDDEV`, `STDDEVP`, `VAR` e `VARP`.

{{% alert color="primary" %}}
La modifica di `Function` influisce solo sull'aggregato, la colonna di origine non cambia.
{{% /alert %}}

Puoi quindi lasciare un campo dati come `SUM` mentre aggiungi un secondo campo dati che ha come destinazione la stessa colonna di origine ma utilizza `COUNT` o `AVERAGE`, tutto in un'unica tabella pivot.

## Visualizzazione dei Campi Valore sull'Asse Riga o Colonna

Quando una tabella pivot contiene due o più campi dati, Aspose.Cells espone un campo virtuale aggiuntivo chiamato `PivotTable.ValuesField`. Questo campo virtuale rappresenta l'aggregato di ogni campo dati presente nell'area dati. Puoi trascinarlo nell'area Riga o Colonna come campo pivot di base, utile per disporre più misure fianco a fianco.

{{% alert color="primary" %}}
`PivotTable.ValuesField` non funziona se non è presente alcun campo valore o se ne è presente solo uno.
{{% /alert %}}

Gli scenari seguenti illustrano tre esempi end-to-end che dimostrano ciascuna delle funzionalità descritte sopra sulla stessa struttura pivot.

## Scenario 1 — Trascinamento di un Campo Base nell'Area Valore

Questo scenario mostra come inserire un singolo campo base (`Amount`) nell'area dati di una tabella pivot esistente. La struttura pivot condivisa posiziona `Category` e `Item` sull'asse Riga e `Year` sull'asse Colonna. Dopo l'operazione, `Amount` appare nell'area dati e viene calcolato come `Sum` di `Amount` per impostazione predefinita.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

## Scenario 2 — Modifica della Funzione di Riepilogo

Questo scenario parte dalla stessa struttura pivot dello Scenario 1 ma aggiunge il campo `Amount` all'area dati due volte. Entrambi i campi dati fanno riferimento alla stessa colonna di origine, tuttavia il secondo campo viene sovrascritto utilizzando il setter `PivotField.Function` in modo che diventi `Count` invece del `Sum` predefinito.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT

pivot_table.calculate_data()
workbook.save("output_function.xlsx")
```

## Scenario 3 — Visualizzazione dei Campi Valore sull'Asse Riga o Colonna

Con due campi dati in posizione, `PivotTable.ValuesField` diventa utilizzabile. Questo scenario trascina quel campo virtuale aggregato nell'area Colonna in modo che ogni misura nell'area dati appaia come un proprio blocco di colonna accanto a `Year`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```

Insieme, questi tre scenari coprono ogni aspetto della manipolazione dei campi valore in Aspose.Cells for Python via Java, da un singolo campo dati con il `Sum` predefinito a una tabella pivot multi-misura in cui il `ValuesField` virtuale controlla il layout sull'asse Riga o Colonna.

## Articoli Correlati

- [Campi Riga e Colonna delle Tabelle Pivot in Aspose.Cells for Python via Java](/cells/it/python-java/row-and-column-fields/)
- [Campi Pagina nelle Tabelle Pivot](/cells/it/python-java/add-page-field-in-pivot-table/)
- [Aggiornamento delle Tabelle Pivot in Aspose.Cells for Python via Java](/cells/it/python-java/refresh-pivot-table/)
- [Applicazione di Stili alle Tabelle Pivot](/cells/it/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}
