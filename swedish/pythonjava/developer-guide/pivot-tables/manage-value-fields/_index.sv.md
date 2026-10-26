---
title: Värdefält i Aspose.Cells for Python via Java
description: Lär dig hur du lägger till basfält i dataregionen i en pivottabell, ändrar sammanfattningsfunktionen med PivotField.Function och visar värdefältet på rad- eller kolumnaxeln i Aspose.Cells for Python via Java.
linktitle: Värdefält i Aspose.Cells for Python via Java
keywords: Aspose.Cells, Python via Java, pivottabell, värdefält, PivotField, PivotField.Function, datafält, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /sv/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Lägga till ett fält i dataregionen
Att lägga till ett basfält i data- (värde-)regionen är det första steget i att forma hur en pivottabell aggregerar din källdata. Aspose.Cells exponerar `PivotTable.addFieldToArea(PivotFieldType, string)`, en överlagring som accepterar konstanten `PivotFieldType.DATA` och källkolonnens namn. När ett fält har lagts till i dataregionen exponerar API:t det via samlingen `PivotTable.DataFields`, i den ordning som fälten lades till. Som standard sammanfattas en numerisk källkolumn med `ConsolidationFunction.SUM`, medan en icke-numerisk kolumn som standard blir `COUNT`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
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
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_table = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
workbook.save("output_drag.xlsx")
jpype.shutdownJVM()
```

## Ändra sammanfattningsfunktionen
Varje fält som placeras i dataregionen omsluts internt som en `PivotField`-instans, och dess `Function`-egenskap returnerar ett värde från enum `ConsolidationFunction`. Samma `Function`-setter låter dig växla mellan tillgängliga aggregat, inklusive `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STDDEV`, `STDDEVP`, `VAR` och `VARP`.

{{% alert color="primary" %}}
Att ändra `Function` påverkar bara aggregatet, källkolumnen ändras inte.
Du kan därför lämna ett datafält som `SUM` medan du lägger till ett andra datafält som riktar sig mot samma källkolumn men använder `COUNT` eller `AVERAGE`, allt i en enda pivot.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, ConsolidationFunction
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
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
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_table = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT)
pivot_table.calculateData()
workbook.save("output_function.xlsx")
jpype.shutdownJVM()
```

## Visa värdefält på rad- eller kolumnaxeln
När en pivottabell innehåller två eller flera datafält exponerar Aspose.Cells ett ytterligare virtuellt fält kallat `PivotTable.ValuesField`. Detta virtuella fält representerar aggregatet av alla datafält som finns i dataregionen. Du kan dra det till rad- eller kolumnregionen som ett baspivotfält, vilket är användbart för att lägga ut flera mått sida vid sida.

{{% alert color="primary" %}}
`PivotTable.ValuesField` fungerar inte om det inte finns något eller endast ett värdefält.
Scenarierna nedan går igenom tre heltäckande exempel som demonstrerar varje funktion som beskrivs ovan mot samma pivotstruktur.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, ConsolidationFunction
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
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
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_table = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT)
pivot_table.addFieldToArea(PivotFieldType.COLUMN, pivot_table.getValuesField())
pivot_table.calculateData()
workbook.save("output_plot.xlsx")
jpype.shutdownJVM()
```

{{< app/cells/assistant language="python" >}}