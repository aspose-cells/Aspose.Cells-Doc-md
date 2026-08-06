---
title: Ändra sidfältslayout i pivottabell
linktitle: Ändra sidfältslayout i pivottabell
description: Lär dig hur du styr layouten för sidfältsområdet i en pivottabell med Aspose.Cells for Python via .NET, inklusive inställning av visningsordning, radbrytningsantal och fältordning för sidfälten överst i pivottabellen.
keywords: Aspose.Cells, Python via .NET-bibliotek, kalkylblad, pivottabell, sidfält, sidfältsordning, sidfältets radbrytningsantal, flytta sidfält
type: docs
weight: 191
url: /sv/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Den här artikeln är en fortsättning på ämnet **Lägg till sidfält i pivottabell**. Den visar hur du styr layouten för sidfältsområdet — remsan med filterkontroller överst i en pivottabell — inklusive visningsordning, radbrytningsantal och omordning av fält.
{{% /alert %}}
## **Introduktion**
En pivottabell i Microsoft Excel har ett dedikerat **sidfältsområde** som sitter ovanför tabellens rad-/kolumn-/datakropp. Det här området renderas som en remsa med rullgardinsfilterkontroller (en per sidfält) och det är vad slutanvändarna klickar på för att segmentera pivoten efter kriterier som år eller region. Aspose.Cells for Python via .NET modellerar detta område via samlingen `pivot_table.page_fields` och exponerar tre egenskaper som styr hur remsan visuellt läggs ut:
- `pivot_table.page_field_order` (ett `PrintOrderType`-värde) avgör om ytterligare sidfält placeras *bredvid* de befintliga eller *under* dem.
- `pivot_table.page_field_wrap_count` anger hur många sidfält som placeras per rad eller kolumn innan radbrytning sker.
- `pivot_table.page_fields.move(curr_index, dest_index)` omordnar sidfälten utan att ändra ordningsläget.
Den här artikeln går igenom tre kodexempel som demonstrerar var och en av dessa operationer på en delad datamängd, så att du kan jämföra de resulterande layouterna sida vid sida.
## **Källdata**
Alla tre exempel nedan läser in dessa åtta rader försäljningsdata i ett kalkylblad med namnet `PivotData`. Datan innehåller två sidfältskandidater (`Year`, `Region`), en radfältskandidat (`Fruit`) och ett mått (`Amount`), vilket gör att sidfältsremsan är meningsfull att inspektera.
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
Alla åtta raderna fylls i i varje kodexempel, i identisk ordning, så att källdatan aldrig skiljer sig åt mellan scenarierna — det är bara sidfältets layoutegenskaper som skiljer sig åt.
## **Exempel 1: Över sedan ned**
I det första scenariot konfigurerar vi de två sidfälten (`Year`, `Region`) så att de visas **sida vid sida i en enda rad** överst i pivottabellen. Vi tilldelar `Fruit` till radaxeln, placerar `Year` först och `Region` därefter på sidaxeln (ordningen på `add_field_to_area`-anropen bestämmer startindexet), lägger till `Amount` (Summa) som datafält och anger sedan `page_field_order` till `PrintOrderType.OverThenDown` med `page_field_wrap_count = 2`. Med `OverThenDown` och ett radbrytningsantal på 2 läggs de två sidfälten ut horisontellt sida vid sida i en enda rad överst i pivottabellen, så att remsan upptar en rad med bredden två.
```python
import os
import aspose.cells as ac

data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)

workbook = ac.Workbook()
worksheets = workbook.worksheets

pivot_data_idx = worksheets.add("PivotData")
pivot_data_sheet = worksheets[pivot_data_idx]
pivot_data_cells = pivot_data_sheet.cells

# Rubriker (rad 0)
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")

# Rad 1: Apple, 2022, North, 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)

# Rad 2: Apple, 2023, North, 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)

# Rad 3: Banana, 2022, South, 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)

# Rad 4: Banana, 2023, South, 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)

# Rad 5: Cherry, 2022, East, 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)

# Rad 6: Cherry, 2023, East, 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)

# Rad 7: Grape, 2022, West, 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)

# Rad 8: Grape, 2023, West, 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)

# Lägg till bladet PivotTableReport
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables

# Skapa pivottabell med källa från PivotData!A1:D9 placerad vid A1 på PivotTableReport
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Lägg till fält
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # Fruit
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # Year
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # Region
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # Amount
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM

# Konfigurera layout för sidfältsområde: placera sidfält först horisontellt, radbryt efter varannan
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

# Uppdatera och beräkna
pivot_table.calculate_data()

# Spara
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```
## **Exempel 2: Ned sedan över**
I det här exemplet placerar vi `Fruit` på radaxeln, `Year` och `Region` på sidaxeln (med `Year` först), och `Amount` (Summa) som datafält — exakt som i Exempel 1. Vi anger sedan `page_field_order` till `PrintOrderType.DownThenOver` och `page_field_wrap_count` till `2`. Med `DownThenOver` och ett radbrytningsantal på 2 staplas de två sidfälten vertikalt — `Year` överst, `Region` direkt under — och bildar en enda kolumn överst i pivottabellen. Remsan upptar alltså två rader med bredden ett, till skillnad från Exempel 1.
```python
import aspose.cells as ac

workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report_idx = workbook.worksheets.add("PivotTableReport")
pivot_report = workbook.worksheets[pivot_report_idx]

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells[0, c].put_value(headers[c])

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
        pivot_data.cells[r + 1, c].put_value(data[r][c])

idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2

pivot_table.calculate_data()

workbook.save("pageFieldLayout_downThenOver.xlsx")
```
## **Exempel 3: Flytta ett sidfält**
I det tredje scenariot behåller vi denna datamängd och fälttilldelning, anger en neutral layout (`OverThenDown` med radbrytningsantal `2`) och demonstrerar sedan `page_fields.move`-operationen. Anropet `move(0, 1)` flyttar sidfältet vid index 0 (`Year`) till position 1, och sidfältet som var vid position 1 (`Region`) flyttas till position 0. Efter detta anrop är `Region` det första sidfältet och `Year` det andra. Radbrytningen och ordningsläget är oförändrade, så remsan renderas fortfarande horisontellt sida vid sida — det är bara ordningen på de två rullgardinsmenyerna som har bytts.
```python
import aspose.cells as ac

workbook = ac.Workbook()

data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"

data_sheet.cells["A1"].put_value("Fruit")
data_sheet.cells["B1"].put_value("Year")
data_sheet.cells["C1"].put_value("Region")
data_sheet.cells["D1"].put_value("Amount")

data_sheet.cells["A2"].put_value("Apple")
data_sheet.cells["B2"].put_value(2022)
data_sheet.cells["C2"].put_value("North")
data_sheet.cells["D2"].put_value(150)

data_sheet.cells["A3"].put_value("Apple")
data_sheet.cells["B3"].put_value(2023)
data_sheet.cells["C3"].put_value("North")
data_sheet.cells["D3"].put_value(180)

data_sheet.cells["A4"].put_value("Banana")
data_sheet.cells["B4"].put_value(2022)
data_sheet.cells["C4"].put_value("South")
data_sheet.cells["D4"].put_value(120)

data_sheet.cells["A5"].put_value("Banana")
data_sheet.cells["B5"].put_value(2023)
data_sheet.cells["C5"].put_value("South")
data_sheet.cells["D5"].put_value(140)

data_sheet.cells["A6"].put_value("Cherry")
data_sheet.cells["B6"].put_value(2022)
data_sheet.cells["C6"].put_value("East")
data_sheet.cells["D6"].put_value(200)

data_sheet.cells["A7"].put_value("Cherry")
data_sheet.cells["B7"].put_value(2023)
data_sheet.cells["C7"].put_value("East")
data_sheet.cells["D7"].put_value(220)

data_sheet.cells["A8"].put_value("Grape")
data_sheet.cells["B8"].put_value(2022)
data_sheet.cells["C8"].put_value("West")
data_sheet.cells["D8"].put_value(90)

data_sheet.cells["A9"].put_value("Grape")
data_sheet.cells["B9"].put_value(2023)
data_sheet.cells["C9"].put_value("West")
data_sheet.cells["D9"].put_value(110)

pivot_sheet_idx = workbook.worksheets.add("PivotTableReport")
pivot_sheet = workbook.worksheets[pivot_sheet_idx]

pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

pivot_table.page_fields.move(0, 1)

pivot_table.calculate_data()

workbook.save("pageFieldLayout_move.xlsx")
```
## **Relaterade artiklar**
- [Lägg till sidfält i pivottabell](/cells/sv/python-net/add-page-field-in-pivot-table/) — föräldrasidan som introducerar hur sidfält läggs till i en pivottabell.
- [Rad- och kolumnfält i pivottabell](/cells/sv/python-net/row-and-column-fields/) — behandlar allokering av fält till rad- och kolumnaxlarna och kompletterar sidaxelarbetet som visas här.
- [Hantera värdefält i pivottabell](/cells/sv/python-net/manage-value-fields/) — beskriver hur dataområdet (värde) konfigureras, inklusive den `Sum`-aggregering som används i denna artikel.
- [Uppdatera pivottabell](/cells/sv/python-net/refresh-pivot-table/) — förklarar `refresh_data` och `calculate_data`, som krävs efter omordning av sidfält.
- [Tillämpa stil på pivottabell](/cells/sv/python-net/apply-style-to-pivot-table/) — visar hur du formaterar den renderade pivottabellen efter att sidfältsremsan har lagts ut.
{{< app/cells/assistant language="python-net" >}}