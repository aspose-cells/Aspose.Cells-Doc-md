---
title: Formatera en del av en pivottabell
linktitle: Formatera en del av en pivottabell
description: Formatera en del av en pivottabell i Aspose.Cells for Python via Java genom att applicera stilar på semantiska PivotArea‑regioner eller CellArea‑rektanglar via PivotTable.format, med formaten lagrade i PivotTable.getPivotFormats() och bevarade när pivottabellen uppdateras.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, pivottabell, format, PivotArea, CellArea, PivotTable.format, getPivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Python
type: docs
weight: 20
url: /sv/python-java/format-part-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
`PivotTable.formatAll` tillämpar en enda stil på hela pivottabellen och behandlas på föräldrasidan. Den skiljer inte mellan etiketter, värden, totaler eller specifika områden i rapporten.
I praktiken behöver bara en del av en pivottabell vanligtvis framhävas. Vanliga mål inkluderar etiketter som tillhör ett radfält, värdeceller som produceras av ett fält, totalraden eller en godtycklig rektangel som de två första elementraderna.
Att applicera en stil direkt på kalkylbladscellerna i en pivottabell är inte ekvivalent. Excel lagrar pivottabellsformatering som semantiska `PivotArea`‑regioner snarare än som vanliga cellstils‑poster. Ett pivot‑områdeformat förblir knutet till en region, till exempel ett fälts etiketter eller datavärden, och återupplöses när pivottabellen beräknas om, uppdateras eller utökas. En stil som skrivs direkt till en cell tillhör däremot den specifika cellpositionen och spåras inte av pivottabellsmodellen.
Aspose.Cells exponerar den kompletta `PivotTable.format`‑överladdningsfamiljen så att båda typerna av formatering är tillgängliga:
- `format(PivotArea, Style)` fäster en stil på en semantisk region som byggs med `PivotArea.select` eller `PivotArea.selectField`.
- `format(CellArea, Style)` fäster en stil på en kalkylbladsrektangel inne i pivottabellen.
- `format(int row, int column, Style)` riktar sig mot en cell.
- `formatAll(Style)` formaterar hela pivottabellen.

## **Formatera ett Pivot‑område**
Arbetssättet med semantiskt område är den rekommenderade metoden när en markering måste följa ett fält eller en region i rapporten.
1. Skapa ett `PivotArea` med `PivotArea(pivot_table)`. Objektet beskriver en semantisk region som tillhör den specifika pivottabellen.
2. Välj ett fält efter dess nollbaserade position på en given axel med `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` väljer både fältets etiketter och data.
   - `PivotTableSelectionType.LABEL_ONLY` väljer endast fältets etiketter.
   - `PivotTableSelectionType.DATA_ONLY` väljer endast fältets dataceller.
3. Välj ett fält efter namn med `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. När ett radfält väljs efter namn löser regionen upp till de värdeceller som produceras av fältets objekt.
4. Skapa en `Style` med `workbook.createStyle()`, konfigurera dess teckensnitt, förgrundsfärg och solid bakgrundsmönster, och skicka stilen till `PivotTable.format(area, style)`.
5. Varje anrop av `PivotArea`‑överladdningen lägger till ett `PivotTableFormat`‑objekt i `PivotTable.getPivotFormats()`.
6. Fältförankrade format appliceras när pivottedatan beräknas. Därför bör du anropa `PivotTable.calculateData()` efter att formaten har applicerats så att stilarna blir synliga.
Följande exempel bygger en liten pivottabell för fruktförsäljning, formaterar `Fruit`‑radetiketterna med `PivotArea.select` och `PivotTableSelectionType.LABEL_ONLY`, formaterar värdecellerna som produceras av samma radfält med `PivotArea.selectField`, och beräknar sedan pivottabellen på nytt så att båda stilarna appliceras.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Style,
    Color,
    BackgroundType,
    PivotArea,
    PivotFieldType,
    PivotTableSelectionType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Bold yellow fill on the row field's label cells
label_style = workbook.createStyle()
label_style.getFont().setBold(True)
label_style.setForegroundColor(Color.getYellow())
label_style.setPattern(BackgroundType.SOLID)
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.createStyle()
value_style.setForegroundColor(Color.getLightGreen())
value_style.setPattern(BackgroundType.SOLID)
value_area = PivotArea(pivot_table)
value_area.selectField(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculateData()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Formatera ett Cell‑område i pivottabellen**
Använd `PivotTable.format(CellArea, Style)` när intresseområdet är en enkel kalkylbladsrektangel snarare än ett semantiskt pivot‑område.
Ett `CellArea` beskrivs av egenskaperna `getStartRow()`, `getStartColumn()`, `getEndRow()` och `getEndColumn()`. Värdena är nollbaserade kalkylbladskoordinater, och slutkoordinaterna anger den sista raden och kolumnen som ingår i rektangeln, så området täcker cellerna från startpositionen till slutpositionen inklusive.
Till skillnad från ett fältförankrat format appliceras ett `CellArea`‑format på cellerna omedelbart. Ett extra anrop av `PivotTable.calculateData()` behövs inte för att stilen ska visas.
En `CellArea`‑rektangel kan innehålla både etikettceller och värdeceller. Nästa avsnitt beskriver hur Aspose.Cells och Excel representerar den rektangeln internt.
Följande exempel formaterar rektangeln `E4:F5` i pivottabellen med en kursiv, ljusblå stil och sparar arbetsboken utan ytterligare omberäkning.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    BackgroundType,
    CellArea,
    PivotFieldType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
jpype.shutdownJVM()
```

## **Hur Pivot‑områden och Cell‑områden mappar**
Excel lagrar pivottabellsformatering som `pivotArea`‑poster snarare än som vanliga kalkylbladscell‑stilsposter. Samma modell används av Aspose.Cells, så en formateringsbegäran översätts till pivot‑områden när den registreras.
Relationen mellan det `CellArea` som användaren tillhandahåller och de pivot‑områden som lagras internt är många‑till‑många i båda riktningarna.
- Ett `CellArea` kan producera flera pivot‑områden. Om rektangeln omfattar både etikettceller och värdeceller delas den upp i separata etikett- och dataregler, eftersom pivottomodellen behandlar etikettformatering och dataformatering oberoende.
- Ett pivot‑område kan lösas upp till flera skilda `CellArea`‑instanser. En semantisk region som en totalrad, eller ett fält vars objekt inte är sammanhängande, kan omfatta flera rektanglar. Detta är anledningen till att `PivotArea.getCellAreas()` returnerar en samling istället för en enstaka rektangel.
Varje formateringsåtgärd som utförs via `PivotTable.format` registreras i `PivotTable.getPivotFormats()`. Varje `PivotTableFormat`‑post exponerar den associerade `PivotArea` och den `Style` som appliceras på den. `PivotArea`‑överladdningen lägger till exakt ett inlägg per anrop, medan ett `CellArea` som innehåller olika semantiska regioner kan lägga till flera inlägg.
För att skilja på de lagrade regionerna exponerar varje `PivotArea` flaggorna `getOnlyLabel()` och `getOnlyData()`. Exemplet nedan formaterar en enstaka rektangel som täcker både etiketter och värden, inspekterar `PivotTable.getPivotFormats()` och skriver ut `CellArea`‑koordinaterna som varje lagrat pivot‑område löser upp till.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import Color, CellArea, Style, BackgroundType
from asposecells.api import PivotTable, PivotArea, PivotFieldType
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
# ONE rectangle in...
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print("Stored formats: " + str(pivot_table.getPivotFormats().getCount()))
for i in range(pivot_table.getPivotFormats().getCount()):
    stored_area = pivot_table.getPivotFormats().get(i).getPivotArea()
    print(
        f"Format {i}: OnlyLabel={stored_area.getOnlyLabel()}, "
        f"OnlyData={stored_area.getOnlyData()}"
    )
    for resolved in stored_area.getCellAreas():
        print(
            f"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, "
            f"columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}"
        )
# This prints:
# Stored formats: 2
# Format 0: OnlyLabel=True, OnlyData=False
#     rows 4-5, columns 5-5        (E4:E5, the label part)
# Format 1: OnlyLabel=False, OnlyData=True
#     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
Eftersom formaten lagras som pivot‑områden snarare än som vanliga cellstilar, överlever de omberäkning och uppdatering. När pivottabellen uppdateras med `PivotTable.refreshData()`, beräknas på nytt med `PivotTable.calculateData()`, eller sparas och läses in igen, löser varje lagrat pivot‑område upp till den aktuella positionen för sin region och dess stil appliceras på nytt.
{{% /alert %}}

Använd ett `PivotArea` byggt med `select` eller `selectField` när en markering måste förbli knuten till ett fält eller en semantisk region över uppdateringar, och använd ett `CellArea` när formatering av en fast rektangel i det aktuella pivottabellslayoutet är tillräckligt. Enstegs‑`format(int row, int column, Style)`‑överladdning riktar sig mot en enskild cell. Använd `formatAll`, som behandlas på föräldrasidan, när hela pivottabellen ska stiliseras om på en gång.

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/python-java/apply-style-to-pivot-table/)
- [Lägga till rad‑ och kolumnfält i pivottabell](/cells/sv/python-java/pivot-table-add-row-and-column-fields/)
- [Hantera värdefält i pivottabell](/cells/sv/python-java/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}