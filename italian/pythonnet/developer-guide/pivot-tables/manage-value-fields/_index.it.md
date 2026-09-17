---
title: Gestire i campi valore di una tabella pivot in Aspose.Cells per .NET
description: Scopri come aggiungere campi di base all'area dati di una tabella pivot, modificare la funzione di riepilogo con PivotField.function e visualizzare il campo valore sull'asse Riga o Colonna in Aspose.Cells for Python via .NET.
linktitle: Campi valore
keywords: Aspose.Cells, Python via .NET, tabella pivot, campo valore, PivotField, PivotField.function, campo dati, PivotTable.values_field, Somma, Media
type: docs
weight: 230
url: /it/python-net/manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Aggiunta di un campo all'area dati
L'aggiunta di un campo di base all'area dati (valore) è il primo passo per definire come una tabella pivot aggrega i dati di origine. Aspose.Cells espone `PivotTable.add_field_to_area(PivotFieldType, str)`, un overload che accetta la costante `PivotFieldType.DATA` e il nome della colonna di origine. Una volta aggiunto un campo all'area dati, l'API lo espone tramite la raccolta `PivotTable.data_fields`, nell'ordine in cui i campi sono stati aggiunti. Per impostazione predefinita, una colonna di origine numerica viene riassunta con `ConsolidationFunction.SUM`, mentre una colonna non numerica utilizza `Count` come valore predefinito.

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
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field)
pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```

## Modifica della funzione di riepilogo
Ogni campo posizionato nell'area dati è incapsulato internamente come istanza di `PivotField` e la sua proprietà `function` restituisce un valore dall'enum `ConsolidationFunction`. Lo stesso setter `function` consente di passare tra gli aggregati disponibili, tra cui `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` e `Varp`.

{{% alert color="primary" %}}
La modifica di `function` influisce solo sull'aggregato, la colonna di origine non cambia.
{{% /alert %}}

È quindi possibile lasciare un campo dati come `Sum` mentre si aggiunge un secondo campo dati che ha come destinazione la stessa colonna di origine ma utilizza `Count` o `Average`, il tutto in un'unica tabella pivot.

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
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
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

## Visualizzazione dei campi valore sull'asse Riga o Colonna
Quando una tabella pivot contiene due o più campi dati, Aspose.Cells espone un campo virtuale aggiuntivo chiamato `PivotTable.values_field`. Questo campo virtuale rappresenta l'aggregato di ogni campo dati presente nell'area dati. È possibile trascinarlo nell'area Riga o Colonna come campo pivot di base, utile per disporre più misure affiancate.

{{% alert color="primary" %}}
`PivotTable.values_field` non funziona se non ci sono campi valore o se ne è presente solo uno.
{{% /alert %}}

Gli scenari seguenti illustrano tre esempi end-to-end che dimostrano ciascuna delle funzionalità descritte sopra sulla stessa struttura di tabella pivot.

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
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

{{< app/cells/assistant language="python-net" >}}