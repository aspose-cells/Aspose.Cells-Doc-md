---
title: Hantera värdefält i en pivottabell i Aspose.Cells för .NET
linktitle: Värdefält
description: Lär dig hur du lägger till basfält i dataregionen i en pivottabell, ändrar summeringsfunktionen med PivotField.function och placerar värdefältet på rad- eller kolumnaxeln i Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, pivottabell, värdefält, PivotField, PivotField.function, datafält, PivotTable.values_field, Sum, Average
type: docs
weight: 230
url: /sv/python-net/pivot-table-manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Lägga till ett fält i dataregionen
Att lägga till ett basfält i data- (värde-)regionen är det första steget för att forma hur en pivottabell aggregerar dina källdata. Aspose.Cells exponerar `PivotTable.add_field_to_area(PivotFieldType, str)`, en överlagring som accepterar konstanten `PivotFieldType.DATA` och källkolumnens namn. När ett fält har lagts till i dataregionen exponerar API:et det via samlingen `PivotTable.data_fields`, i den ordning som fälten lades till. Som standard sammanfattas en numerisk källkolumn med `ConsolidationFunction.SUM`, medan en icke-numerisk kolumn som standard blir `Count`.
## Ändra summeringsfunktionen
Varje fält som placeras i dataregionen omsluts internt som en `PivotField`-instans, och dess egenskap `function` returnerar ett värde från enum `ConsolidationFunction`. Samma `function`-setter låter dig växla mellan de tillgängliga aggregaten, inklusive `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` och `Varp`.
{{% alert color="primary" %}}
Att ändra `function` påverkar bara aggregatet, källkolumnen ändras inte.
{{% /alert %}}
Du kan därför låta ett datafält vara kvar som `Sum` medan du lägger till ett andra datafält som riktar sig mot samma källkolumn men använder `Count` eller `Average`, allt i en enda pivot.
## Placera värdefält på rad- eller kolumnaxeln
När en pivottabell innehåller två eller fler datafält exponerar Aspose.Cells ett ytterligare virtuellt fält kallat `PivotTable.values_field`. Detta virtuella fält representerar aggregatet av varje datafält som finns i dataregionen. Du kan dra det till rad- eller kolumnregionen som ett baspivotfält, vilket är användbart för att lägga ut flera mått sida vid sida.
{{% alert color="primary" %}}
`PivotTable.values_field` fungerar inte om det inte finns något eller bara ett värdefält.
{{% /alert %}}
Scenarierna nedan går igenom tre kompletta exempel som demonstrerar varje funktionalitet som beskrivs ovan mot samma pivotstruktur.
## Scenario 1 — Dra ett basfält till värdeområdet
Detta scenario visar hur man placerar ett enskilt basfält (`Amount`) i dataregionen för en befintlig pivottabell. Den delade pivotstrukturen placerar `Category` och `Item` på radaxeln och `Year` på kolumnaxeln. Efter åtgärden visas `Amount` i dataregionen och beräknas som standard som `Sum` av `Amount`.
```python
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Rubriker i A1:D1
worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

# Datarader A2:D9 med nästlade slingor som förgrenar sig på j
for i in range(1, 9):
    for j in range(4):
        if j == 0:
            worksheet.cells[i, j].put_value("Fruit" if i <= 4 else "Vegetable")
        elif j == 1:
            if i == 1 or i == 2:
                worksheet.cells[i, j].put_value("Apple")
            elif i == 3 or i == 4:
                worksheet.cells[i, j].put_value("Banana")
            elif i == 5 or i == 6:
                worksheet.cells[i, j].put_value("Carrot")
            else:
                worksheet.cells[i, j].put_value("Daikon")
        elif j == 2:
            worksheet.cells[i, j].put_value(2020 + ((i - 1) % 2))
        elif j == 3:
            if i == 1:
                worksheet.cells[i, j].put_value(100)
            elif i == 2:
                worksheet.cells[i, j].put_value(150)
            elif i == 3:
                worksheet.cells[i, j].put_value(80)
            elif i == 4:
                worksheet.cells[i, j].put_value(90)
            elif i == 5:
                worksheet.cells[i, j].put_value(50)
            elif i == 6:
                worksheet.cells[i, j].put_value(60)
            elif i == 7:
                worksheet.cells[i, j].put_value(40)
            else:
                worksheet.cells[i, j].put_value(45)

# Lägg till pivottabell vid F3 med namnet PivotTable1
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Pivotlayout: Kategori och Objekt på Rad, År på Kolumn, Belopp som datafält
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```
## Scenario 2 — Ändra summeringsfunktionen
Detta scenario utgår från samma pivotstruktur som Scenario 1 men lägger till fältet `Amount` i dataregionen två gånger. Båda datafälten refererar till samma källkolumn, men det andra fältet åsidosätts med hjälp av `PivotField.function`-settern så att det blir `Count` istället för standardvärdet `Sum`.
```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")

pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

count_field = pivot_table.data_fields[1]
count_field.function = ac.ConsolidationFunction.COUNT

pivot_table.calculate_data()

workbook.save("output_function.xlsx")
```
## Scenario 3 — Placera värdefält på rad- eller kolumnaxeln
Med två datafält på plats blir `PivotTable.values_field` användbar. Detta scenario drar det virtuella aggregatfältet till kolumnregionen så att varje mått i dataregionen visas som sitt eget kolumnblock bredvid `Year`.
```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ac.ConsolidationFunction.COUNT

# Plotta värdefälten på kolumnaxeln.
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()

workbook.save("output_plot.xlsx")
```
Tillsammans täcker dessa tre scenarier varje aspekt av värdefältsmanipulation i Aspose.Cells for Python via .NET, från ett enskilt datafält med standardvärdet `Sum` till en pivot med flera mått där det virtuella `ValuesField` styr layouten på rad- eller kolumnaxeln.

{{< app/cells/assistant language="python" >}}
