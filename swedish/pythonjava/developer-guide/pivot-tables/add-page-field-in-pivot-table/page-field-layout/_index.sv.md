---
title: Ändra sidfältslayout i pivottabell
linktitle: Ändra sidfältslayout i pivottabell
description: Lär dig hur du styr layouten för sidfältsområdet i en pivottabell med Aspose.Cells for Python via Java, inklusive att ställa in visningsordning, radbrytningsantal och fältordning för sidfälten överst i pivottabellen.
keywords: Aspose.Cells for Python via Java, Python Java-bibliotek, kalkylblad, pivottabell, sidfält, ordning för sidfält, radbrytningsantal för sidfält, flytta sidfält
type: docs
weight: 191
url: /sv/python-java/change-page-field-layout/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Den här artikeln är en fortsättning på ämnet **Lägg till sidfält i pivottabell**. Den visar hur du styr layouten för sidfältsområdet — remsan med filterkontroller överst i en pivottabell — inklusive visningsordning, radbrytningsantal och omordning av fält.
{{% /alert %}}
## **Introduktion**
En pivottabell i Microsoft Excel har ett dedikerat **sidfältsområde** som sitter ovanför tabellens rad-/kolumn-/datakropp. Det här området renderas som en remsa med rullgardinsfilterkontroller (en per sidfält) och det är vad slutanvändare klickar på för att filtrera pivoten efter kriterier som år eller region. Aspose.Cells for Python via Java modellerar det här området via samlingen `pivot_table.page_fields` och exponerar tre egenskaper som styr hur remsan visas visuellt:
- `pivot_table.page_field_order` (ett `Aspose.Cells.PrintOrderType`-värde) avgör om ytterligare sidfält placeras *bredvid* de befintliga eller *under* dem.
- `pivot_table.page_field_wrap_count` anger hur många sidfält som placeras per rad eller kolumn innan radbrytning sker.
- `pivot_table.page_fields.move(curr_index, dest_index)` omordnar sidfälten utan att ändra orderläget.
Den här artikeln går igenom tre kodexempel som demonstrerar var och en av dessa operationer på en delad datamängd, så att du kan jämföra de resulterande layouterna sida vid sida.
## **Källdata**
Alla tre exemplen nedan läser in dessa åtta rader försäljningsdata till ett kalkylblad med namnet `PivotData`. Datan innehåller två sidfältskandidater (`Year`, `Region`), en radfältskandidat (`Fruit`) och ett mått (`Amount`), vilket gör att sidfältsremsan blir meningsfull att granska.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Alla åtta rader fylls i varje kodexempel, i identisk ordning, så källdatan skiljer sig aldrig mellan scenarierna — bara egenskaperna för sidfältslayouten gör det.
## **Exempel 1: Över sedan ner**
I det första scenariot konfigurerar vi de två sidfälten (`Year`, `Region`) så att de visas **sida vid sida i en enda rad** överst i pivottabellen. Vi tilldelar `Fruit` till radaxeln, placerar `Year` först och `Region` därefter på sidaxeln (ordningen på anropen till `add_field_to_area` bestämmer startindexet), lägger till `Amount` (Summa) som datafält och anger sedan `page_field_order` till `PrintOrderType.OVER_THEN_DOWN` med `page_field_wrap_count = 2`. Med `OVER_THEN_DOWN` och ett radbrytningsantal på 2 läggs de två sidfälten ut horisontellt sida vid sida i en enda rad överst i pivottabellen, så att remsan upptar en rad med bredden två.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorksheetCollection, Worksheet, Cells, PivotTableCollection, PivotTable, PivotFieldType, ConsolidationFunction, PrintOrderType

dataDir = "output"
if not os.path.exists(dataDir):
    os.makedirs(dataDir, exist_ok=True)

workbook = Workbook()
worksheets = workbook.getWorksheets()

pivotDataIdx = worksheets.add("PivotData")
pivotDataSheet = worksheets.get(pivotDataIdx)
pivotDataCells = pivotDataSheet.getCells()

# Rubriker (rad 0)
pivotDataCells.get(0, 0).putValue("Fruit")
pivotDataCells.get(0, 1).putValue("Year")
pivotDataCells.get(0, 2).putValue("Region")
pivotDataCells.get(0, 3).putValue("Amount")

# Rad 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple")
pivotDataCells.get(1, 1).putValue(2022)
pivotDataCells.get(1, 2).putValue("North")
pivotDataCells.get(1, 3).putValue(150)

# Rad 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple")
pivotDataCells.get(2, 1).putValue(2023)
pivotDataCells.get(2, 2).putValue("North")
pivotDataCells.get(2, 3).putValue(180)

# Rad 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana")
pivotDataCells.get(3, 1).putValue(2022)
pivotDataCells.get(3, 2).putValue("South")
pivotDataCells.get(3, 3).putValue(120)

# Rad 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana")
pivotDataCells.get(4, 1).putValue(2023)
pivotDataCells.get(4, 2).putValue("South")
pivotDataCells.get(4, 3).putValue(140)

# Rad 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry")
pivotDataCells.get(5, 1).putValue(2022)
pivotDataCells.get(5, 2).putValue("East")
pivotDataCells.get(5, 3).putValue(200)

# Rad 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry")
pivotDataCells.get(6, 1).putValue(2023)
pivotDataCells.get(6, 2).putValue("East")
pivotDataCells.get(6, 3).putValue(220)

# Rad 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape")
pivotDataCells.get(7, 1).putValue(2022)
pivotDataCells.get(7, 2).putValue("West")
pivotDataCells.get(7, 3).putValue(90)

# Rad 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape")
pivotDataCells.get(8, 1).putValue(2023)
pivotDataCells.get(8, 2).putValue("West")
pivotDataCells.get(8, 3).putValue(110)

# Lägg till PivotTableReport-blad
pivotTableSheetIdx = worksheets.add("PivotTableReport")
pivotTableSheet = worksheets.get(pivotTableSheetIdx)
pivotTables = pivotTableSheet.getPivotTables()

# Skapa pivottabell från PivotData!A1:D9 placerad vid A1 på PivotTableReport
pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Lägg till fält
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)   # Frukt
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)  # År
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)  # Region
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)  # Belopp
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM)

# Konfigurera layout för sidfältsområde: placera sidfält horisontellt först, radbryt efter var 2:a
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

# Uppdatera och beräkna
pivotTable.calculateData()

# Spara
workbook.save(os.path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"))

jpype.shutdownJVM()
```
## **Exempel 2: Ner sedan över**
I det här exemplet placerar vi `Fruit` på radaxeln, `Year` och `Region` på sidaxeln (med `Year` först) och `Amount` (Summa) som datafält — exakt som i Exempel 1. Vi anger sedan `page_field_order` till `PrintOrderType.DOWN_THEN_OVER` och `page_field_wrap_count` till `2`. Med `DOWN_THEN_OVER` och ett radbrytningsantal på 2 staplas de två sidfälten vertikalt — `Year` överst, `Region` direkt under — och bildar en enda kolumn överst i pivottabellen. Remsan upptar därför två rader med bredden ett, i motsats till Exempel 1.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PrintOrderType

workbook = Workbook()
pivotData = workbook.getWorksheets().get(0)
pivotData.setName("PivotData")
pivotReportIdx = workbook.getWorksheets().add("PivotTableReport")
pivotReport = workbook.getWorksheets().get(pivotReportIdx)

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivotData.getCells().get(0, c).putValue(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivotData.getCells().get(r + 1, c).putValue(data[r][c])

idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable")
pivotTable = pivotReport.getPivotTables().get(idx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)
pivotTable.setPageFieldWrapCount(2)

pivotTable.calculateData()

workbook.save("pageFieldLayout_downThenOver.xlsx")

jpype.shutdownJVM()
```
## **Exempel 3: Flytta ett sidfält**
I det tredje scenariot behåller vi den här datamängden och fälttilldelningen, anger en neutral layout (`OVER_THEN_DOWN` med radbrytningsantal `2`) och demonstrerar sedan operationen `page_fields.move`. Anropet `move(0, 1)` flyttar sidfältet vid index 0 (`Year`) till position 1, och sidfältet som var på position 1 (`Region`) flyttas till position 0. Efter det här anropet är `Region` det första sidfältet och `Year` det andra. Radbrytningen och ordningsläget är oförändrade, så remsan renderas fortfarande horisontellt sida vid sida — bara ordningen på de två rullgardinsmenyerna har bytts ut.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PrintOrderType

workbook = Workbook()

dataSheet = workbook.getWorksheets().get(0)
dataSheet.setName("PivotData")

dataSheet.getCells().get("A1").putValue("Fruit")
dataSheet.getCells().get("B1").putValue("Year")
dataSheet.getCells().get("C1").putValue("Region")
dataSheet.getCells().get("D1").putValue("Amount")

dataSheet.getCells().get("A2").putValue("Apple")
dataSheet.getCells().get("B2").putValue(2022)
dataSheet.getCells().get("C2").putValue("North")
dataSheet.getCells().get("D2").putValue(150)

dataSheet.getCells().get("A3").putValue("Apple")
dataSheet.getCells().get("B3").putValue(2023)
dataSheet.getCells().get("C3").putValue("North")
dataSheet.getCells().get("D3").putValue(180)

dataSheet.getCells().get("A4").putValue("Banana")
dataSheet.getCells().get("B4").putValue(2022)
dataSheet.getCells().get("C4").putValue("South")
dataSheet.getCells().get("D4").putValue(120)

dataSheet.getCells().get("A5").putValue("Banana")
dataSheet.getCells().get("B5").putValue(2023)
dataSheet.getCells().get("C5").putValue("South")
dataSheet.getCells().get("D5").putValue(140)

dataSheet.getCells().get("A6").putValue("Cherry")
dataSheet.getCells().get("B6").putValue(2022)
dataSheet.getCells().get("C6").putValue("East")
dataSheet.getCells().get("D6").putValue(200)

dataSheet.getCells().get("A7").putValue("Cherry")
dataSheet.getCells().get("B7").putValue(2023)
dataSheet.getCells().get("C7").putValue("East")
dataSheet.getCells().get("D7").putValue(220)

dataSheet.getCells().get("A8").putValue("Grape")
dataSheet.getCells().get("B8").putValue(2022)
dataSheet.getCells().get("C8").putValue("West")
dataSheet.getCells().get("D8").putValue(90)

dataSheet.getCells().get("A9").putValue("Grape")
dataSheet.getCells().get("B9").putValue(2023)
dataSheet.getCells().get("C9").putValue("West")
dataSheet.getCells().get("D9").putValue(110)

pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport")
pivotSheet = workbook.getWorksheets().get(pivotSheetIdx)

pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable")
pivotTable = pivotSheet.getPivotTables().get(pivotIdx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

pivotTable.getPageFields().move(0, 1)

pivotTable.calculateData()

workbook.save("pageFieldLayout_move.xlsx")

jpype.shutdownJVM()
```
## **Relaterade artiklar**
- [Lägg till sidfält i pivottabell](/cells/sv/python-java/add-page-field-in-pivot-table/) — föräldrasidan som introducerar hur sidfält läggs till i en pivottabell.
- [Rad- och kolumnfält i pivottabell](/cells/sv/python-java/row-and-column-fields/) — täcker tilldelning av fält till rad- och kolumnaxlarna och kompletterar sidaxelarbetet som visas här.
- [Hantera värdefält i pivottabell](/cells/sv/python-java/manage-value-fields/) — beskriver hur man konfigurerar data- (värde) området, inklusive `SUM`-aggregeringen som används i den här artikeln.
- [Uppdatera pivottabell](/cells/sv/python-java/refresh-pivot-table/) — förklarar `refresh_data` och `calculate_data`, som krävs efter omordning av sidfält.
- [Tillämpa stil på pivottabell](/cells/sv/python-java/apply-style-to-pivot-table/) — visar hur man formaterar den renderade pivottabellen efter att sidfältsremsan har lagts ut.
{{< app/cells/assistant language="python" >}}