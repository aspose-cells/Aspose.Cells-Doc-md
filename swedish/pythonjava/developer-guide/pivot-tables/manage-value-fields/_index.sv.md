---
title: Värdefält i Aspose.Cells for Python via Java
linktitle: Värdefält i Aspose.Cells for Python via Java
description: Lär dig hur du lägger till basfält i dataregionen i en pivottabell, ändrar sammanfattningsfunktionen med PivotField.Function och visar värdefältet på rad- eller kolumnaxeln i Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, pivottabell, värdefält, PivotField, PivotField.Function, datafält, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /sv/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Värdefält är kärnan i varje pivottabell – de numeriska aggregaten som sammanfattar källdatan. I Aspose.Cells for Python via Java fylls dataregionen i en pivottabell genom att lägga till basfält via `PivotTable.addFieldToArea`, och varje fält som placeras i den regionen kan ha sin egen sammanfattningsfunktion. När två eller flera datafält finns exponerar Aspose.Cells ett särskilt aggregatfält, `PivotTable.ValuesField`, som kan visas på rad- eller kolumnaxeln som ett basfält, vilket ger dig finare kontroll över hur värdefält visas i layouten.

## Lägga till ett fält i dataregionen

Att lägga till ett basfält i data- (värde-)regionen är det första steget i att forma hur en pivottabell aggregerar din källdata. Aspose.Cells exponerar `PivotTable.addFieldToArea(PivotFieldType, string)`, en överlagring som accepterar konstanten `PivotFieldType.DATA` och källkolonnens namn. När ett fält har lagts till i dataregionen exponerar API:t det via samlingen `PivotTable.DataFields`, i den ordning som fälten lades till. Som standard sammanfattas en numerisk källkolumn med `ConsolidationFunction.SUM`, medan en icke-numerisk kolumn som standard blir `COUNT`.

## Ändra sammanfattningsfunktionen

Varje fält som placeras i dataregionen omsluts internt som en `PivotField`-instans, och dess `Function`-egenskap returnerar ett värde från enum `ConsolidationFunction`. Samma `Function`-setter låter dig växla mellan tillgängliga aggregat, inklusive `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STDDEV`, `STDDEVP`, `VAR` och `VARP`.

{{% alert color="primary" %}}
Att ändra `Function` påverkar bara aggregatet, källkolumnen ändras inte.
{{% alert %}}

Du kan därför lämna ett datafält som `SUM` medan du lägger till ett andra datafält som riktar sig mot samma källkolumn men använder `COUNT` eller `AVERAGE`, allt i en enda pivot.

## Visa värdefält på rad- eller kolumnaxeln

När en pivottabell innehåller två eller flera datafält exponerar Aspose.Cells ett ytterligare virtuellt fält kallat `PivotTable.ValuesField`. Detta virtuella fält representerar aggregatet av alla datafält som finns i dataregionen. Du kan dra det till rad- eller kolumnregionen som ett baspivotfält, vilket är användbart för att lägga ut flera mått sida vid sida.

{{% alert color="primary" %}}
`PivotTable.ValuesField` fungerar inte om det inte finns något eller endast ett värdefält.
{{% alert %}}

Scenarierna nedan går igenom tre heltäckande exempel som demonstrerar varje funktion som beskrivs ovan mot samma pivotstruktur.

## Scenario 1 — Dra ett basfält till värdeområdet

Detta scenario visar hur man placerar ett enskilt basfält (`Amount`) i dataregionen för en befintlig pivottabell. Den delade pivotstrukturen placerar `Category` och `Item` på radaxeln och `Year` på kolumnaxeln. Efter operationen visas `Amount` i dataregionen och beräknas som `Sum` av `Amount` som standard.

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

pivot_table.refresh_data()
pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

## Scenario 2 — Ändra sammanfattningsfunktionen

Detta scenario utgår från samma pivotstruktur som Scenario 1 men lägger till fältet `Amount` i dataregionen två gånger. Båda datafälten refererar till samma källkolumn, men det andra fältet åsidosätts med `PivotField.Function`-settern så att det blir `Count` istället för standardvärdet `Sum`.

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

pivot_table.refresh_data()
pivot_table.calculate_data()
workbook.save("output_function.xlsx")
```

## Scenario 3 — Visa värdefält på rad- eller kolumnaxeln

Med två datafält på plats blir `PivotTable.ValuesField` användbart. Detta scenario drar det aggregerade virtuella fältet till kolumnregionen så att varje mått i dataregionen visas som sitt eget kolumnblock bredvid `Year`.

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

pivot_table.refresh_data()
pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```

Tillsammans täcker dessa tre scenarion varje aspekt av värdefältsmanipulation i Aspose.Cells for Python via Java, från ett enskilt datafält med standardvärdet `Sum` till en pivot med flera mått där det virtuella `ValuesField` styr layouten på rad- eller kolumnaxeln.

## Relaterade artiklar

- [Pivottabellens rad- och kolumnfält i Aspose.Cells for Python via Java](/cells/sv/python-java/row-and-column-fields/)
- [Sidfält i pivottabeller](/cells/sv/python-java/add-page-field-in-pivot-table/)
- [Uppdatera pivottabeller i Aspose.Cells for Python via Java](/cells/sv/python-java/refresh-pivot-table/)
- [Tillämpa stilar på pivottabeller](/cells/sv/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}