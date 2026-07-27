---
title: Lägga till rad- och kolumnfält i en pivottabell i Aspose.Cells för .NET
linktitle: Rad- och kolumnfält
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /sv/python-java/pivot-table-add-row-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


Rad- och kolumnfält är byggstenarna i en pivottabell. Ett fält som placeras i radregionen visas vertikalt till vänster i pivottabellen, medan ett fält som placeras i kolumnregionen visas horisontellt överst. Den här artikeln visar hur man lägger till basfält i dessa regioner programmatiskt och hur man styr delsummorna som renderas mellan fältgrupper med hjälp av metoden `PivotField.setSubtotals`.

## **Lägga till ett fält i rad- eller kolumnregionen**

Metoden `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` flyttar ett basfält från källdatan till en av de fyra pivotregionerna. Argumentet `fieldType` accepterar ett av följande `PivotFieldType`-värden.

- `ROW` — fält som placeras vertikalt till vänster
- `COLUMN` — fält som placeras horisontellt överst
- `DATA` — fält vars värden aggregeras
- `PAGE` — fält som används som rapportfilter

När fält har lagts till kan du komma åt dem via metoderna `PivotTable.getRowFields()` och `PivotTable.getColumnFields()`. Varje metod returnerar en `PivotFieldCollection`. Fältet på index 0 i `RowFields` är det yttersta radfältet, och efterföljande index representerar fält som är nästlade inuti det. Samma indexkonvention gäller för `ColumnFields`.

Ordningen på fältnästning spelar roll. Att lägga till `Category` i radregionen först och sedan `Item` skapar en pivot vars yttre gruppering är `Category` och vars inre gruppering är `Item`. Att vända på ordningen vänder på hierarkin.

## **Pivotfältets delsummor**

Metoden `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` styr vilka delsummarader som visas för ett pivotfält. Varje anrop växlar en enskild delsummatyp oberoende. Att skicka `shown = true` visar delsummoraden, medan `shown = false` döljer den. Eftersom varje anrop endast påverkar en typ, bygger upprepade anrop med olika `subtotalType`-värden en anpassad delmängd av delsummor.

Enumen `PivotFieldSubtotalType` definierar de tillgängliga typerna av delsummor.

- `AUTOMATIC` — Aspose.Cells väljer standardvalet (vanligtvis `SUM` för numeriska fält)
- `NONE` — undertryck alla delsummarader
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
Delsummor renderas endast när det finns två eller fler pivotfält i radregionen (eller i kolumnregionen). Ett enskilt fält har inget meningsfullt att beräkna delsummor mellan, så anrop till `setSubtotals` har ingen synlig effekt i det fallet. Den här artikeln placerar därför två radfält (`Category` ytterst, `Item` innerst) i varje exempel så att delsummogränsen mellan varje `Category`-grupp är synlig.
{{% /alert %}}

## **Scenario 1 — Automatiska (standard) delsummor**

När du inte anropar `setSubtotals` alls, tillämpar Aspose.Cells valet `AUTOMATIC` på numeriska fält. Följande exempel bekräftar uttryckligen detta beteende genom att anropa `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` på det yttre `Category`-radfältet.

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

## **Scenario 2 — Undertrycka alla delsummor (None)**

Att anropa `setSubtotals(PivotFieldSubtotalType.NONE, true)` tar bort varje delsummarad från pivottabellen och lämnar endast fältraderna och totalsumman längst ner. Detta är användbart när du vill ha den råa grupperade datan utan några sammanfattningsrader.

```python
ells
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

## **Scenario 3 — Anpassad delmängd av delsummor (Sum + Average)**

Du är inte begränsad till en enskild delsummatyp. Varje `setSubtotals`-anrop verkar oberoende på en typ, så att anropa metoden två gånger — en gång med `SUM` och en gång med `AVERAGE` — skapar en anpassad delmängd av två delsummarader för varje `Category`-grupp.

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
## **Sammanfattning**

De tre scenarierna ovan delar samma dataset och pivottabellstruktur. Den enda skillnaden mellan dem är `setSubtotals`-anropet som tillämpas på det yttre `Category`-radfältet. Kom ihåg tvåfältsregeln: ett enskilt fält i en region har inget att beräkna delsummor mellan, så placera alltid minst två fält i rad- eller kolumnregionen när du vill att `setSubtotals` ska ha en synlig effekt.

## **Relaterade artiklar**

- [Page Fields in Pivot Tables](/cells/sv/python-java/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Python via Java](/cells/sv/python-java/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/sv/python-java/apply-style-to-pivot-table/)
Looking at the original document carefully:

The CODE_BLOCK comments are HTML comment placeholders with descriptions. The instruction says: "HTML Comment Placeholders (CRITICAL): The document contains `<!-- CODE_BLOCK:N:... -->` HTML comments. These are CODE BLOCK PLACEHOLDERS — you MUST preserve them EXACTLY as-is in your translation. Do NOT remove, modify, or translate them."



Also, I need to make sure the assistant shortcode is preserved exactly: ``

The title is: "Row and Column Fields in Aspose.Cells for Python via Java"
This contains the product name "Aspose.Cells for Python via Java" which must be preserved exactly.

So the title stays exactly as: "Row and Column Fields in Aspose.Cells for Python via Java"

That's correct - I'm not translating it because it contains the product name which must stay.

"ONLY translate the VALUES of title, description, and keywords."

But also: "The following product names must appear EXACTLY as-is throughout the document"

These don't conflict. I should translate the parts that aren't product names. So "Row and Column Fields" can be translated.



But the title contains the product name. If I translate "Row and Column Fields" to "Rad- och kolumnfält", then I'd have:
"Rad- och kolumnfält in Aspose.Cells for Python via Java"

This should be fine. The product name "Aspose.Cells for Python via Java" appears exactly once.


And linktitle:
"Rad- och kolumnfält"



title: "Rad- och kolumnfält i Aspose.Cells for Python via Java"
linktitle: Rad- och kolumnfält
description: "Lär dig hur du lägger till basfält i rad- och kolumnregionerna i en pivottabell och styr pivotfältets delsummor med PivotField.setSubtotals i Aspose.Cells for Python via Java"
keywords: "Aspose.Cells, Python via Java, pivottabell, radfält, kolumnfält, PivotField, setSubtotals, PivotFieldSubtotalType, delsummor"

Translated: "Lär dig hur du lägger till basfält i rad- och kolumnregionerna i en pivottabell och styr pivotfältets delsummor med PivotField.setSubtotals i Aspose.Cells for Python via Java."

No colons in this translation. Good.

- All API names: ✓
- All enum values: ✓
- All method names: ✓
- All shortcodes: ✓
- All HTML comments: ✓
- All URLs: ✓

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

jpype.shutdownJVM()python
ells
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

jpype.shutdownJVM()python
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

jpype.shutdownJVM()These must be preserved exactly as-is.

Rad- och kolumnfält är byggstenarna i en pivottabell. Ett fält som placeras i radregionen visas vertikalt till vänster i pivottabellen, medan ett fält som placeras i kolumnregionen visas horisontellt överst. Den här artikeln visar hur man lägger till basfält i dessa regioner programmatiskt och hur man styr delsummorna som renderas mellan fältgrupper med hjälp av metoden `PivotField.setSubtotals`.

## **Lägga till ett fält i rad- eller kolumnregionen**

Metoden `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` flyttar ett basfält från källdatan till en av de fyra pivotregionerna. Argumentet `fieldType` accepterar ett av följande `PivotFieldType`-värden.

- `ROW` — fält som placeras vertikalt till vänster
- `COLUMN` — fält som placeras horisontellt överst
- `DATA` — fält vars värden aggregeras
- `PAGE` — fält som används som rapportfilter

När fält har lagts till kan du komma åt dem via metoderna `PivotTable.getRowFields()` och `PivotTable.getColumnFields()`. Varje metod returnerar en `PivotFieldCollection`. Fältet på index 0 i `RowFields` är det yttersta radfältet, och efterföljande index representerar fält som är nästlade inuti det. Samma indexkonvention gäller för `ColumnFields`.

Ordningen på fältnästning spelar roll. Att lägga till `Category` i radregionen först och sedan `Item` skapar en pivot vars yttre gruppering är `Category` och vars inre gruppering är `Item`. Att vända på ordningen vänder på hierarkin.

## **Pivotfältets delsummor**

Metoden `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` styr vilka delsummarader som visas för ett pivotfält. Varje anrop växlar en enskild delsummatyp oberoende. Att skicka `shown = true` visar delsummoraden, medan `shown = false` döljer den. Eftersom varje anrop endast påverkar en typ, bygger upprepade anrop med olika `subtotalType`-värden en anpassad delmängd av delsummor.

Enumen `PivotFieldSubtotalType` definierar de tillgängliga typerna av delsummor.

- `AUTOMATIC` — Aspose.Cells väljer standardvalet (vanligtvis `SUM` för numeriska fält)
- `NONE` — undertryck alla delsummarader
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
Delsummor renderas endast när det finns två eller fler pivotfält i radregionen (eller i kolumnregionen). Ett enskilt fält har inget meningsfullt att beräkna delsummor mellan, så anrop till `setSubtotals` har ingen synlig effekt i det fallet. Den här artikeln placerar därför två radfält (`Category` ytterst, `Item` innerst) i varje exempel så att delsummogränsen mellan varje `Category`-grupp är synlig.
{{% /alert %}}

## **Scenario 1 — Automatiska (standard) delsummor**

När du inte anropar `setSubtotals` alls, tillämpar Aspose.Cells valet `AUTOMATIC` på numeriska fält. Följande exempel bekräftar uttryckligen detta beteende genom att anropa `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` på det yttre `Category`-radfältet.## **Scenario 2 — Undertrycka alla delsummor (None)**

Att anropa `setSubtotals(PivotFieldSubtotalType.NONE, true)` tar bort varje delsummarad från pivottabellen och lämnar endast fältraderna och totalsumman längst ner. Detta är användbart när du vill ha den råa grupperade datan utan några sammanfattningsrader.## **Scenario 3 — Anpassad delmängd av delsummor (Sum + Average)**

Du är inte begränsad till en enskild delsummatyp. Varje `setSubtotals`-anrop verkar oberoende på en typ, så att anropa metoden två gånger — en gång med `SUM` och en gång med `AVERAGE` — skapar en anpassad delmängd av två delsummarader för varje `Category`-grupp.## **Sammanfattning**

De tre scenarierna ovan delar samma dataset och pivottabellstruktur. Den enda skillnaden mellan dem är `setSubtotals`-anropet som tillämpas på det yttre `Category`-radfältet. Kom ihåg tvåfältsregeln: ett enskilt fält i en region har inget att beräkna delsummor mellan, så placera alltid minst två fält i rad- eller kolumnregionen när du vill att `setSubtotals` ska ha en synlig effekt.

## **Relaterade artiklar**

- [Page Fields in Pivot Tables](/cells/sv/python-java/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Python via Java](/cells/sv/python-java/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/sv/python-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
