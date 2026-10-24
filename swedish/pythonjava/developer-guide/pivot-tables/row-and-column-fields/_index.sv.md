---
title: Lägg till pivottabellens rad- och kolumnfält i Aspose.Cells for Python via Java
linktitle: Lägg till pivottabellens rad- och kolumnfält i Aspose.Cells for Python via Java
description: Lär dig hur du lägger till basfält i pivottabellens rad- och kolumnområden och styr pivotfältets delsummor med PivotField.setSubtotals i Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, pivottabell, radfält, kolumnfält, PivotField, setSubtotals, PivotFieldSubtotalType, delsummor
type: docs
weight: 220
url: /sv/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Lägga till ett fält i rad- eller kolumnområdet**
Metoden `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` flyttar ett basfält från källdatan till ett av de fyra pivotområdena. Argumentet `fieldType` accepterar ett av följande `PivotFieldType`-värden.
- `ROW` — fält som placeras vertikalt till vänster
- `COLUMN` — fält som placeras horisontellt överst
- `DATA` — fält vars värden aggregeras
- `PAGE` — fält som används som rapportfilter
Fältens nästlingsordning spelar roll. Att lägga till `Category` i radområdet först och `Item` sedan skapar en pivottabell med `Category` som yttre gruppering och `Item` som inre gruppering. Att vända ordningen inverterar hierarkin.

## **Delsummor för pivotfält**
Metoden `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` styr vilka delsummarader som visas för ett pivotfält. Varje anrop styr en enskild delsummatyp oberoende av övriga typer. `shown = true` visar delsummoraden, medan `shown = false` döljer den. Eftersom varje anrop endast påverkar en typ skapar upprepade anrop med olika `subtotalType`-värden en anpassad delmängd av delsummor.
Enumet `PivotFieldSubtotalType` definierar de tillgängliga delsummatyperna.
- `AUTOMATIC` — Aspose.Cells väljer standardvalet (vanligtvis `SUM` för numeriska fält)
- `NONE` — undertrycker alla delsummarader
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
Delsummor visas endast när det finns två eller flera pivotfält i radområdet (eller i kolumnområdet). Ett enda fält ger ingen meningsfull grund för att beräkna delsummor mellan grupper, och anrop till `setSubtotals` har därför ingen synlig effekt i det fallet. Denna artikel placerar därför två radfält (`Category` ytterst, `Item` innerst) i varje exempel så att gränsen till delsummorna i varje `Category`-grupp blir synlig.
{{% /alert %}}

## **Scenario 1 — Automatiska delsummor (standard)**
Om du inte anropar `setSubtotals` alls, tillämpar Aspose.Cells valet `AUTOMATIC` på numeriska fält. Följande exempel bekräftar uttryckligen detta beteende genom att anropa `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` på det yttre radfältet `Category`.

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
pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
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

## **Scenario 2 — Dölja alla delsummor (inga)**
Att anropa `setSubtotals(PivotFieldSubtotalType.NONE, true)` tar bort alla delsummarader från pivottabellen och lämnar endast fältraderna och totalsumman längst ned. Det är användbart när du vill se den grupperade rådatan utan sammanfattningsrader.

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
pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
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

## **Scenario 3 — Anpassad delmängd av delsummor (Summa + Medelvärde)**
Du är inte begränsad till en enda delsummatyp. Varje anrop till `setSubtotals` påverkar oberoende en delsummatyp, så att två anrop till metoden — ett med `SUM` och ett med `AVERAGE` — ger en anpassad delmängd av två delsummarader för varje `Category`-grupp.

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
pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)
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

## **Sammanfattning**

De tre scenarierna skiljer sig bara i en sak: `setSubtotals`-anropen. Allt annat – datamängden, fälten och de områden de tilldelas till – är identiskt, vilket gör att layouterna kan jämföras direkt.
- **Placera fält.** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` flyttar en källkolumn till ett område. Inom ett område är anropens ordning den visuella ordningen, så det första anroppet blir den yttre gruppen. Subtotaler kräver två eller fler fält i samma område: med ett enda fält finns det inget mellan grupperna att summera.
- **Scenario 1 – automatiska subtotaler.** Om `setSubtotals` inte anropas lämnas valet till Excel, som tillämpar sin egen standardsubtotal för numeriska fält. Om `setSubtotals` anropas med `PivotFieldSubtotalType.AUTOMATIC` registreras detta val explicit istället för att lämna det implicit.
- **Scenario 2 – inga subtotaler.** `setSubtotals` med `PivotFieldSubtotalType.NONE` inaktiverar standardsubtotalkonfigurationen, så pivottabellen behåller fältrowerna och grandtotalkolumnen men utelämnar de subtotalrader som Excel annars skulle infoga mellan dem.
- **Scenario 3 – ett valt utvalt subtotalset.** Varje anrop växlar exakt en subtotaltyp, och anropen akkumuleras snarare än att återställa varandra. Om du anropar den en gång med `PivotFieldSubtotalType.SUM` och en gång med `PivotFieldSubtotalType.AVERAGE` är båda aktiverade, och pivottabellen visar en `Sum`-subtotal, en `Average`-subtotal och en `grand total`.

{{% alert color="primary" %}}
Inget vid subtotaler är specifikt för radområdet. Samma `setSubtotals`-anrop på ett fält taget från `PivotTable.ColumnFields` ger samma tre layouter på kolomaxeln, eftersom inställningen hör till pivottabellfältet snarare än till axeln det placeras på.
{{% /alert %}}
## **Relaterade artiklar**
- [Sidfält i pivottabeller](/cells/sv/python-java/add-page-field-in-pivot-table/)
- [Uppdatera pivottabeller i Aspose.Cells for Python via Java](/cells/sv/python-java/refresh-pivot-table/)
- [Tillämpa stilar på pivottabeller](/cells/sv/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}