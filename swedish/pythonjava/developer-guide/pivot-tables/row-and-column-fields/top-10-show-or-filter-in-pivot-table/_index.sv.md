---
title: Visa eller filtrera topp 10 i pivottabell
linktitle: Visa eller filtrera topp 10 i pivottabell
description: Lär dig hur du endast visar de högst eller lägst rankade objekten i ett pivotfält med Aspose.Cells for Python via Java. Artikeln beskriver metoden top10AutoShow i Excel 97-2003, hur du läser alternativen med Top10AutoShowSettings och filtret topp 10 i Excel 2007-365 via filterTop10.
keywords: Aspose.Cells for Python via Java, pivottabell, topp 10, AutoShow, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /sv/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell som listar alla objekt i ett radfält kan vara svårt att läsa när fältet har tiotals objekt. En topp 10-rapport behåller endast de högst eller lägst rankade objekten, vilket är precis vad rankningsrapporter behöver – ”de fem produkterna med högst intäkt” eller ”de tre regionerna med lägst antal försäljningar”. Aspose.Cells stöder två mekanismer för detta, och de motsvarar två generationer av Microsoft Excel.
- **Excel 97-2003 AutoShow** – metoden `PivotField.top10AutoShow()`. Detta är den klassiska inställningen ”Visa de översta/understa N objekten” som lagras direkt på pivotfältet. Den fungerar i alla Excel-versioner, både äldre och nyare, eftersom den ingår i pivottabellens ursprungliga format.
- **Excel 2007-365 topp 10-filter** – metoden `PivotField.filterTop10()`. Detta är det moderna topp 10-värdefiltret som finns under Värdefiltrar i fältmenyn. Det lagras som ett `PivotFilter`-objekt som är kopplat till fältet och erbjuder rankning baserad på antal objekt eller procent.

## **Visa topp 10 i Excel 97-2003 (top10AutoShow)**
Den klassiska AutoShow-inställningen konfigureras med ett enda anrop till `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` – aktiverar eller inaktiverar AutoShow-inställningen på fältet.
- `isTop` – `True` behåller de högst rankade objekten (topp), `False` behåller de lägst rankade (botten).
- `count` – hur många objekt som ska behållas, till exempel 10 för en klassisk topp 10-rapport.
- `rankBy` – det nollbaserade indexet för det **datafält** vars värden används för att rangordna objekten. Ange -1 för att rangordna objekten efter fältet självt.
Rankningen kan baseras på ett värdefält eller på fältet självt. Det finns två möjliga varianter, som visas nedan.

### **Rankning efter ett värdefält**
Rangordna radfältets objekt efter ett vanligt värdefält, till exempel `Sum of Sales`. Det följande exemplet bygger en pivottabell med ett radfält (`Sport`) och ett datafält (`Sales`) och visar sedan de två sporten med högst försäljning. `rankBy` är 0 eftersom `Sum of Sales` är datafältet med index 0.

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
sport_field.setAutoShow(True)
sport_field.setAutoShowCount(2)
sport_field.setAutoShowField(2)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Rankning efter fältet självt**
Ett fält kan även rangordnas efter sig självt – ange -1 som `rankBy`. För denna variant behövs inget extra datafält; fältet behöver endast placeras i rad- eller kolumnområdet. Det följande exemplet visar de tre lägst rankade sporten, rangordnade efter fältet självt. När denna inställning sparas utelämnas attributet `rankBy` från pivottabellens XML eftersom -1 är formatets standardvärde, och `Top10AutoShowSettings.getRankBy()` läser tillbaka -1.

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
# Visa de 3 lägsta objekten rankade efter fältet självt (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Läsa aktuella alternativ (Top10AutoShowSettings)**
Metoden `PivotField.getTop10AutoShowSettings()` returnerar ett `PivotFieldTop10AutoShowSettings`-objekt som exponerar de alternativ för AutoShow som för närvarande lagras på fältet. Använd det för att granska hur objekten kommer att visas i en befintlig arbetsbok eller i en pivottabell som du nyligen konfigurerade – detta gäller även arbetsböcker som har lästs in från en fil.

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

De fyra egenskaperna motsvarar de klassiska AutoShow-attributen som skrivs till pivottabellens XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). De värden som läses tillbaka är därför de värden som alla Excel-versioner respekterar.

## **Obs**

{{% alert color="primary" %}}
- De direkta åtkomstmetoderna för `PivotField`, `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` och `getAutoShowField()`, är markerade som föråldrade. Använd i stället objektet `Top10AutoShowSettings`: `PivotField.isAutoShow()` ersätts av `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` ersätts av `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` ersätts av `Top10AutoShowSettings.getAutoShowCount()` och `PivotField.getAutoShowField()` ersätts av `Top10AutoShowSettings.getRankBy()`. Metoden `top10AutoShow()` är det stödda sättet att ändra inställningarna.
- `top10AutoShow` fungerar med rad- och kolumnfält. Ett fält som endast finns i sidfältsområdet (filterområdet) kan inte rangordnas på detta sätt eftersom dess objekt inte placeras i pivottabellens brödtext.
{{% /alert %}}

## **Excel 2007-365: topp 10-filter (filterTop10)**
Moderna Excel-versioner exponerar topp 10 som ett värdefilter i fältmenyn (Värdefiltrar, Topp 10...). Aspose.Cells modellerar det med metoden `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, som returnerar det skapade `PivotFilter`-objektet:
- `valueFieldIndex` – det nollbaserade indexet för det datafält vars aggregerade värden används för att rangordna objekten.
- `type` – vad `itemCount` betyder. `PivotFilterType.COUNT` behåller ett bestämt antal objekt (alternativet Objekt i dialogrutan). `PivotFilterType.PERCENT` behåller en procentandel av objekten, så att `itemCount` är själva procenttalet – 30 behåller de översta 30 procenten. `PivotFilterType.SUM` rangordnar efter hur stor del av det totala värdet som omfattas.
- `isTop` – `True` för topp, `False` för botten.
- `itemCount` – N i ”Topp N”; enheten beror på `type`.

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
    # Topp 10-filter — behåll de 2 bästa objekten efter "Sum of Sales" (datafältsindex 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # För ett procentbaserat filter i stället, behåll de bästa 30 procenten av objekten:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` och `filterTop10` är två separata funktioner. AutoShow skriver det klassiska `autoShow`-attributet på pivotfältet. Inställningen respekteras av alla Excel-versioner sedan Excel 97. `filterTop10` skriver en modern `PivotFilter`-post, vilket kräver Excel 2007 eller senare. När en arbetsbok öppnas i en äldre Excel-version visar en pivottabell som använder det moderna filtret alla objekt i stället för att filtrera. För dokument som måste gå igenom äldre verktyg utan att inställningarna går förlorade, välj `top10AutoShow`; för moderna arbetsböcker, välj `filterTop10` eftersom filtret kan kombineras med de övriga värdefiltren.
{{% /alert %}}

## **Relaterade artiklar**
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/python-java/filter-by-label-or-value-of-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/python-java/pivot-table-add-row-and-column-fields/)
- [Gruppera pivotfält i pivottabellen](/cells/sv/python-java/group-pivot-fields-in-the-pivot-table/)
- [Uppdatera pivottabellen](/cells/sv/python-java/refresh-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}