---
title: Visa eller filtrera topp 10 i pivottabell
linktitle: Visa eller filtrera topp 10 i pivottabell
description: Lär dig att endast visa de högst eller lägst rankade objekten i ett pivotfält med Aspose.Cells for Python via Java. Den här artikeln beskriver metoden top10AutoShow för Excel 97-2003, hur du läser alternativ med Top10AutoShowSettings och filtret för topp 10 i Excel 2007-365 via filterTop10.
keywords: Aspose.Cells for Python via Java, pivottabell, topp 10, automatisk visning, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /sv/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell som listar varje objekt i ett radfält kan vara svårläst när fältet har dussintals medlemmar. En topp 10-rapport behåller endast de högst eller lägst rankade objekten, vilket är precis vad rankningsrapporter behöver – "topp 5 produkter efter intäkt" eller "de 3 lägst rankade regionerna efter antal försäljningar". Aspose.Cells stöder två mekanismer för detta, och de motsvarar två generationer av Microsoft Excel.
- **Excel 97-2003 AutoShow** – metoden `PivotField.top10AutoShow()`. Detta är den klassiska inställningen "Visa de översta/understa N objekten" som lagras direkt på pivotfältet. Den fungerar i alla Excel-versioner, gamla som nya, eftersom den ingår i det ursprungliga pivottabellformatet.
- **Excel 2007-365 topp 10-filter** – metoden `PivotField.filterTop10()`. Detta är det moderna värdefiltret för topp 10 som finns under Värdefilter i fältmenyn. Det lagras som ett `PivotFilter`-objekt kopplat till fältet och erbjuder rangordning baserad på antal objekt eller procentandel.

## **Visa topp 10 i Excel 97-2003 (top10AutoShow)**
Den klassiska AutoShow-funktionen konfigureras med ett enda anrop till `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` – aktiverar eller inaktiverar AutoShow-inställningen på fältet.
- `isTop` – `True` behåller de högst rankade objekten (topp), `False` behåller de lägst rankade (botten).
- `count` – hur många objekt som ska behållas, till exempel 10 för en klassisk topp 10-rapport.
- `rankBy` – det nollbaserade indexet för det **datafält** vars värden används för att rangordna objekten. Ange -1 för att rangordna objekten efter fältet självt.
Rangordningen kan utgå från ett värdefält eller från fältet självt. Det finns två naturliga varianter, som visas nedan.

### **Rangordna efter ett värdefält**
Rangordna radfältets objekt efter ett vanligt värdefält, till exempel "Summa av försäljning". Följande exempel bygger en pivottabell med ett radfält (`Sport`) och ett datafält (`Sales`) och visar sedan de två sporten med högst försäljning. `rankBy` är 0 eftersom "Summa av försäljning" är datafältet med index 0.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
sport_field.top10AutoShow(True, True, 2, 0)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Rangordna efter fältet självt**
Ett fält kan också rangordna sina egna objekt – ange -1 som `rankBy`. För denna variant behövs inget extra datafält; fältet behöver bara finnas i rad- eller kolumnområdet. Följande exempel visar de tre lägst rankade sporten enligt fältet självt. När inställningen sparas utelämnas attributet `rankBy` från pivottabellens XML eftersom -1 är formatets standardvärde, och `Top10AutoShowSettings.getRankBy()` läser tillbaka -1.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
# Show the bottom 3 items ranked by the field itself (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Läsa aktuella alternativ (Top10AutoShowSettings)**
Metoden `PivotField.getTop10AutoShowSettings()` returnerar ett `PivotFieldTop10AutoShowSettings`-objekt som exponerar de AutoShow-alternativ som för närvarande lagras på fältet. Använd det för att kontrollera hur fältets objekt kommer att presenteras i en befintlig arbetsbok eller i en pivottabell som du nyss har konfigurerat – även när arbetsboken har lästs in från en fil.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
sport_field = pivot_table.getRowFields()[0]
settings = sport_field.getTop10AutoShowSettings()
print("AutoShow enabled: " + str(settings.isAutoShow()))
print("Direction: " + ("Top" if settings.isTop() else "Bottom"))
print("Item count: " + str(settings.getAutoShowCount()))
print("Ranking data field index: " + str(settings.getRankBy()))
jpype.shutdownJVM()
```

De fyra egenskaperna motsvarar de klassiska AutoShow-attributen som skrivs till pivottabellens XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), så att de värden som läses tillbaka är de som alla Excel-versioner tillämpar.

## **Obs**

{{% alert color="primary" %}}
- De direkta `PivotField`-åtkomstmetoderna `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` och `getAutoShowField()` har markerats som föråldrade. Använd `Top10AutoShowSettings`-objektet i stället: `PivotField.isAutoShow()` blir `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` blir `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` blir `Top10AutoShowSettings.getAutoShowCount()` och `PivotField.getAutoShowField()` blir `Top10AutoShowSettings.getRankBy()`. Det stödda sättet att ändra inställningarna är metoden `top10AutoShow()`.
- `top10AutoShow` fungerar med rad- och kolumnfält. Ett fält som endast finns i sidområdet (filterområdet) kan inte rangordnas på detta sätt eftersom dess objekt inte placeras i pivottabellens brödtext.
{{% /alert %}}

## **Excel 2007-365: topp 10-filter (filterTop10)**
Moderna Excel-versioner exponerar topp 10 som ett värdefilter i fältmenyn (Värdefilter, Topp 10...). Aspose.Cells modellerar det med metoden `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, som returnerar det skapade `PivotFilter`-objektet:
- `valueFieldIndex` – det nollbaserade indexet för det datafält vars aggregerade värden används för att rangordna objekten.
- `type` – vad `itemCount` innebär. `PivotFilterType.COUNT` behåller ett bestämt antal objekt (dialogens alternativ Objekt). `PivotFilterType.PERCENT` behåller en viss procentandel av objekten, så `itemCount` är procenttalet självt – 30 behåller de översta 30 procenten. `PivotFilterType.SUM` rangordnar efter hur stor del av det totala värdet som omfattas.
- `isTop` – `True` för topp, `False` för botten.
- `itemCount` – N i topp N; enheten beror på `type`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFilterType
try:
    workbook = Workbook()
    worksheet = workbook.getWorksheets().get(0)
    worksheet.getCells().get("A1").putValue("Sport")
    worksheet.getCells().get("B1").putValue("Quarter")
    worksheet.getCells().get("C1").putValue("Sales")
    sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
    row = 2
    for sport in sports:
        for quarter in range(1, 4):
            worksheet.getCells().get(row, 0).putValue(sport)
            worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
            worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
            row += 1
    pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
    pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
    pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
    pivot_table.calculateData()
    sport_field = pivot_table.getRowFields().get(0)
    # Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # For a percentage-based filter instead, keep the top 30 percent of the items:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` och `filterTop10` är två separata mekanismer. AutoShow skriver den klassiska attributuppsättningen `autoShow` till pivotfältet, och den tillämpas av alla Excel-versioner från Excel 97 och framåt. `filterTop10` skriver en modern `PivotFilter`-post, som kräver Excel 2007 eller senare. När en arbetsbok öppnas i en äldre Excel-version visar en pivottabell som använder det moderna filtret i stället alla objekt. För dokument som måste bearbetas fram och tillbaka med äldre verktyg bör du välja `top10AutoShow`; för moderna arbetsböcker bör du välja `filterTop10` eftersom det kan kombineras med de andra värdefiltren.
{{% /alert %}}

## **Relaterade artiklar**
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/python-java/filter-by-label-or-value-of-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/python-java/pivot-table-add-row-and-column-fields/)
- [Gruppera pivotfält i pivottabellen](/cells/sv/python-java/group-pivot-fields-in-the-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/python-java/refresh-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}