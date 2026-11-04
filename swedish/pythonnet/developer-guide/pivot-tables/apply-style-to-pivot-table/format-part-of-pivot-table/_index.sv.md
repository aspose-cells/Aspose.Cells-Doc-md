---
title: Formatera del av en pivottabell
linktitle: Formatera del av en pivottabell
description: Formatera del av en pivottabell i Aspose.Cells for Python via .NET genom att tillämpa stilar på semantiska PivotArea‑regioner eller CellArea‑rektanglar via PivotTable.format, där formaten lagras i PivotTable.pivot_formats och bevaras när pivottabellen uppdateras.
keywords: Aspose.Cells for Python via .NET, pivottabell, format, PivotArea, CellArea, PivotTable.format, pivot_formats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, select_field, format_all, Python via .NET
type: docs
weight: 20
url: /sv/python-net/format-part-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
`PivotTable.format_all` tillämpar en enda stil på hela pivottabellen och behandlas på föräldrasidan. Den gör ingen skillnad mellan etiketter, värden, totaler eller specifika områden i rapporten.  
I praktiken behöver bara en del av en pivottabell oftast framhävas. Vanliga mål inkluderar etiketter som tillhör ett radfält, värdeceller som skapats av ett fält, totalrad eller en godtycklig rektangel såsom de två första objektraderna.  
Att tillämpa en stil direkt på kalkylbladscellerna i en pivottabell är inte samma sak. Excel lagrar pivottabell‑formatering som semantiska `PivotArea`‑regioner snarare än som vanliga cell‑stilsregister. En pivot‑områdes‑format förblir bifogad till ett område såsom ett fälts etiketter eller datavärden, och den återupptas när pivottabellen beräknas om, uppdateras eller expanderas. En stil som skrivs direkt till en cell hör däremot till den cellpositionen och spåras inte av pivot‑modellen.  
Aspose.Cells exponerar hela familjen av `PivotTable.format`‑overloads så att båda typerna av formatering är tillgängliga:
- `format(PivotArea, Style)` anknyter en stil till en semantisk region som byggs med `PivotArea.select` eller `PivotArea.select_field`.
- `format(CellArea, Style)` anknyter en stil till en kalkylblads‑rektangel i pivottabellen.
- `format(int row, int column, Style)` riktar in sig på en enskild cell.
- `format_all(Style)` formaterar hela pivottabellen.

## **Formatera ett Pivot‑område**
Det semantiska område‑arbetsflödet är det rekommenderade tillvägagångssättet när en markering måste följa ett fält eller ett område i rapporten.
1. Skapa ett `PivotArea` med `PivotArea(pivot_table)`. Objektet beskriver ett semantiskt område som tillhör just den pivottabellen.
1. Välj ett fält genom dess noll‑baserade position på en given axel med `PivotArea.select(PivotFieldType axis_type, int field_position, PivotTableSelectionType selection_type)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` väljer både fältets etiketter och data.
   - `PivotTableSelectionType.LABEL_ONLY` väljer endast fältets etiketter.
   - `PivotTableSelectionType.DATA_ONLY` väljer endast fältets dataceller.
1. Välj ett fält efter namn med `PivotArea.select_field(PivotFieldType axis_type, string field_name)`. När ett radfält väljs efter namn löser området upp sig till de värdeceller som produceras av fältets objekt.
1. Skapa ett `Style` med `Workbook.create_style()`, konfigurera dess teckensnitt, förgrundsfärg och solid bakgrundsmönster, och skicka stilen till `PivotTable.format(area, style)`.
1. Varje anrop till `PivotArea`‑overload lägger till en `PivotTableFormat`‑post i `PivotTable.pivot_formats`.
1. Fältanknutna format målas när pivot‑data beräknas. Därför ska `PivotTable.calculate_data()` anropas efter att formaten har tillämpats så att stilarna blir synliga.  
Följande exempel bygger en liten pivottabell för frukt‑försäljning, formaterar `Fruit`‑radetiketterna med `PivotArea.select` och `PivotTableSelectionType.LABEL_ONLY`, formaterar värdecellerna som produceras av samma radfält med `PivotArea.select_field`, och beräknar sedan pivottabellen på nytt så att båda stilarna målas.

```python
from aspose.cells.pivot import PivotArea, PivotFieldType, PivotTableSelectionType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Bold yellow fill on the row field's label cells
label_style = workbook.create_style()
label_style.font.is_bold = True
label_style.foreground_color = Color.yellow
label_style.pattern = ac.BackgroundType.SOLID
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.create_style()
value_style.foreground_color = Color.light_green
value_style.pattern = ac.BackgroundType.SOLID
value_area = PivotArea(pivot_table)
value_area.select_field(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculate_data()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
```

## **Formatera ett Cell‑område i pivottabellen**
Använd `PivotTable.format(CellArea, Style)` när intresseområdet är en enkel kalkylbladsrektangel snarare än ett semantiskt pivot‑område.  
Ett `CellArea` beskrivas av egenskaperna `start_row`, `start_column`, `end_row` och `end_column`. Värdena är noll‑baserade kalkylbladskoordinater, och slutkoordinaterna identifierar den sista rad och kolumn som inkluderas i rektangeln, så området täcker cellerna från startpositionen till slutpositionen, inklusive.  
Till skillnad från ett fält‑anknutet format appliceras ett `CellArea`‑format omedelbart på cellerna. Ett ytterligare anrop till `calculate_data()` behövs inte för att stilen ska visas.  
En `CellArea`‑rektangel kan innehålla både etikett‑celler och värde‑celler. Nästa avsnitt beskriver hur Aspose.Cells och Excel representerar den rektangeln internt.  
Följande exempel formaterar rektangeln `E4:F5` i pivottabellen med en kursiv, ljusblå stil och sparar arbetsboken utan någon ytterligare omräkning.

```python
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
```

## **Hur Pivot‑områden och Cell‑områden mappar**
Excel lagrar pivottabell‑formatering som `pivotArea`‑poster snarare än som vanliga kalkylblads‑cell‑stilsregister. Samma modell används av Aspose.Cells, så en formateringsbegäran översätts till pivot‑områden när den registreras.  
Relationen mellan det `CellArea` som användaren tillhandahåller och de pivot‑områden som lagras internt är många‑till‑många i båda riktningarna.
- Ett `CellArea` kan producera flera pivot‑områden. Om rektangeln omfattar både etikett‑celler och värde‑celler delas den upp i separata etikett‑ och data‑regler, eftersom pivot‑modellen behandlar etikett‑formatering och data‑formatering oberoende av varandra.
- Ett pivot‑område kan lösas upp i flera separata `CellArea`‑instanser. Ett semantiskt område såsom en rad för totalen, eller ett fält vars objekt inte är samanhörande, kan täcka flera rektanglar. Detta är anledningen till att `PivotArea.get_cell_areas()` returnerar en samling istället för en enskild rektangel.
Varje formatoperation som utförs via `PivotTable.format` registreras i `PivotTable.pivot_formats`. Varje `PivotTableFormat`‑post exponerar det associerade `PivotArea` och den `Style` som tillämpas på det. `PivotArea`‑overload lägger till exakt en post per anrop, medan ett `CellArea` som innehåller olika semantiska regioner kan lägga till flera poster.  
För att skilja på de lagrade regionerna exponerar varje `PivotArea` flaggorna `only_label` och `only_data`. Exemplet nedan formaterar en enda rektangel som täcker både etiketter och värden, inspekterar `PivotTable.pivot_formats` och skriver ut de `CellArea`‑koordinater som varje lagrat pivot‑område löser upp till.

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
# ONE rectangle in...
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print(f"Stored formats: {len(pivot_table.pivot_formats)}")
for i in range(len(pivot_table.pivot_formats)):
    stored_area = pivot_table.pivot_formats[i].pivot_area
    print(f"Format {i}: OnlyLabel={stored_area.only_label}, OnlyData={stored_area.only_data}")
    for resolved in stored_area.get_cell_areas():
        print(
            f"    rows {resolved.start_row + 1}-{resolved.end_row + 1}, "
            f"columns {resolved.start_column + 1}-{resolved.end_column + 1}"
        )
workbook.save("FormatPivotAreasMap.xlsx")
```

{{% alert color="primary" %}}
Eftersom formaten lagras som pivot‑områden snarare än som vanliga cell‑stilar, överlever de omräkningar och uppdateringar. När pivottabellen uppdateras med `PivotTable.refresh_data`, beräknas om med `calculate_data`, eller sparas och läses in igen, återupptas varje lagrat pivot‑område till sin nuvarande positionsområde och stilen tillämpas på nytt.
{{% /alert %}}

Använd ett `PivotArea` byggt med `select` eller `select_field` när en markering måste förbli fäst vid ett fält eller en semantisk region över flera uppdateringar, och använd ett `CellArea` när du formaterar en fast rektangel i den aktuella pivottabellslayouten. Den enkla‑celloverloaden `format(int row, int column, Style)` riktar in sig på en individuell cell. Använd `format_all`, som behandlas på föräldrasidan, när hela pivottabellen ska omformas på en gång.

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/python-net/apply-style-to-pivot-table/)
- [Lägga till rad‑ och kolumnfält i pivottabell](/cells/sv/python-net/pivot-table-add-row-and-column-fields/)
- [Hantera värdefält i pivottabell](/cells/sv/python-net/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}