---
title: Lägg till villkorsstyrd formatering i en pivottabell
linktitle: Lägg till villkorsstyrd formatering i en pivottabell
description: Lägg till villkorsstyrd formatering i en pivottabell i Aspose.Cells for Python via .NET – förankra en regel till dataområdet med apply_to och ett PivotConditionFormatScopeType‑omfång, eller definiera målet med add_cell_area och pivot_areas, och sedan fästa regler och stilar via format_conditions.add_condition.
keywords: Aspose.Cells, Aspose.Cells for Python via .NET, pivottabell, villkorsstyrd formatering, PivotConditionalFormat, conditional_formats, apply_to, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, add_cell_area, pivot_areas, add_pivot_area, format_conditions, add_condition, FormatConditionType, Python
type: docs
weight: 30
url: /sv/python-net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Stilarna som beskrivs på föräldrasidan och på syskonsidan är statiska – ett `PivotArea` eller `CellArea`‑område målas en gång och behåller sin stil oavsett vilka värden som finns. Villkorsstyrd formatering är den regelbaserade motsvarigheten – markera varje belopp över 200, färga de mittersta femtio procenten eller flagga de lägst rankade posterna – och markeringen följer värdena varje gång pivottabellen omräknas eller uppdateras.  
I Aspose.Cells finns villkorsstyrd formatering för pivottabeller i samlingen `pivot_table.conditional_formats`. Varje post är ett `PivotConditionalFormat` som svarar på två frågor oberoende av varandra:
- **Var tillämpas regeln?** Målområdet definieras antingen via `apply_to(row: int, column: int, scope: PivotConditionFormatScopeType)`, vilket speglar omfångsväljaren i Excel‑användargränssnittet, eller via `add_cell_area(cell_area: CellArea)` och samlingen `pivot_areas`, som namnger området explicit.
- **Vad testar regeln?** En eller flera villkor läggs till i `format_conditions` med `format_conditions.add_condition(type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)`, och varje villkor har sin egen `style`.

{{% alert color="primary" %}}
Anropa inte `format_conditions.add(cell_area: CellArea, type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` eller `format_conditions.add_area(cell_area: CellArea)` på `format_conditions`‑objektet för ett pivottabells villkorliga format. Dessa två överlagringar är ärvda från den vanliga kalkylblads‑API:n för villkorsstyrd formatering och fungerar inte för pivottabeller – cellområdet konverteras aldrig till ett pivot‑område, så begäran ignoreras tyst. Definiera alltid området på själva `pivot_conditional_format` (`apply_to`, `add_cell_area` eller `pivot_areas`) och lägg till regeln med någon av `add_condition`‑overlagringarna.
{{% /alert %}}

## **Applicera en regel med ett omfång (Excel‑gränssnittet)**
Det första sättet placerar regeln på samma sätt som Excel‑användargränssnittet. En cell i pivottabellen identifieras med sina nollbaserade kalkylbladskoordinater, och ett `PivotConditionFormatScopeType`‑omfång anger hur långt regeln ska sträcka sig från den cellen:
- `PivotConditionFormatScopeType.DATA` – alla värdeceller som pivottabellen producerar, inklusive totalsummor.
- `PivotConditionFormatScopeType.FIELD` – värdecellerna som tillhör det fält som cellen identifierar, exklusive totalsummor. Cell måste vara en fältcell, till exempel en rad‑fältetikett; att skicka en värdecell kastar ett undantag.
- `PivotConditionFormatScopeType.SELECTION` – endast de värdeceller som finns i skärningspunkten som cellen väljer, vanligtvis en enstaka värdecell.
Exemplet nedan bygger en pivottabell för fruktförsäljning med övre vänstra hörnet i E3, förankrar ett villkorsstyrt format i cell F4 (rad 3, kolumn 5) med `PivotConditionFormatScopeType.DATA`‑omfånget och markerar varje belopp över 200 med fet vit text på rött. Med värdena Apple 220, Banana 330, Cherry 200 och totalsumman 750 färgar regeln F4, F5 och F7 – det upplösta området är hela datakolumnen F4:F7, och endast de celler vars värde uppfyller regeln lyser upp.

```python
from aspose.cells.pivot import PivotFieldType, PivotConditionFormatScopeType
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
# Pivot‑tabell med dess övre vänstra hörn på E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Fäst det villkorliga formatet på F4 (rad 3, kolumn 5) med Data‑omfånget
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
format.apply_to(3, 5, PivotConditionFormatScopeType.DATA)
# Regel – markera belopp som är större än 200
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.GREATER_THAN,
    "200",
    None
)
style = workbook.create_style()
style.font.is_bold = True
style.font.color = Color.white
style.foreground_color = Color.red
style.pattern = ac.BackgroundType.SOLID
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatData.xlsx")
```

Att förankra samma regel på rad‑fältetiketten E4 (rad 3, kolumn 4) med `PivotConditionFormatScopeType.FIELD`‑omfånget ger F4:F6 istället – samma datakolumn utan totalsummoraden – eftersom omfånget nu beskriver fältet `Fruit` snarare än hela värdeområdet. `PivotConditionFormatScopeType.SELECTION`‑omfånget som förankras på F4 ger endast F4.

## **Definiera området manuellt**
Det andra sättet hoppar över omfångsväljaren och namnger området explicit på `PivotConditionalFormat`.

### **Ett kalkylbladsrektangel med add_cell_area**
`add_cell_area(cell_area: CellArea)` registrerar den angivna rektangeln som regelns mål. Koordinaterna är nollbaserade kalkylbladskoordinater, och området är exakt den levererade rektangeln – ingen utvidgning till datakolumnen och ingen totalsummalogik. Använd den när de intressanta cellerna utgör en fast rektangel i den aktuella pivottabellens layout.

```python
from aspose.cells import BackgroundType, FormatConditionType, OperatorType
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
# Markera rektangeln F4:F6 (värdecellerna utan totalsumman)
index = pivot_table.conditional_formats.add()
conditional_format = pivot_table.conditional_formats[index]
area = ac.CellArea()
area.start_row = 3
area.start_column = 5
area.end_row = 5
area.end_column = 5
conditional_format.add_cell_area(area)
# Regel – kursiv på ljusgul för belopp mellan 150 och 300
condition_index = conditional_format.format_conditions.add_condition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300"
)
style = workbook.create_style()
style.font.is_italic = True
style.foreground_color = Color.light_yellow
style.pattern = BackgroundType.SOLID
conditional_format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatCellArea.xlsx")
```

### **Ett semantiskt pivot‑område med pivot_areas**
`pivot_areas` är samma semantiska‑områdesmodell som syskonsidan använder för statiska stilar. Bygg ett `PivotArea`, välj ett fält eller område med `select` eller `select_field`, och lägg till det med `pivot_areas.add_pivot_area(pivot_area)`. Ett semantiskt område förblir fäst vid sitt fält, så den villkorsstyrda formateringen följer fältet när pivottabellen uppdateras och layouten förändras. Överlagringen `pivot_areas.add(pivot_area)` kompilerar fortfarande men är markerad som föråldrad – föredra `add_pivot_area`.

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
# Fäst regeln på datafältet Amount som ett semantiskt område
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
area = ac.PivotArea(pivot_table)
area.select_field(PivotFieldType.DATA, "Amount")
format.pivot_areas.add_pivot_area(area)
# Regel – grå text för belopp under 150
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.LESS_THAN,
    "150",
    None
)
style = workbook.create_style()
style.font.color = Color.gray
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatPivotArea.xlsx")
```

## **Var reglerna lagras och hur de överlever en omladdning**
Varje anrop av `pivot_table.conditional_formats.add()` lägger till ett `PivotConditionalFormat` i pivottabellen. Villkoren, deras formler och deras stilar sparas med arbetsboken – när filen öppnas igen i exemplet nedan visas samma regel med sin typ, operator och formel intakt, och `get_cell_areas()` rapporterar samma områden. Poster som aldrig fick ett villkor tas bort när arbetsboken sparas, på samma sätt som Excel tar bort en villkorsstyrd formatering som saknar regel.

```python
import aspose.cells as ac
workbook = ac.Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
print("Conditional formats: " + str(pivot_table.conditional_formats.count))
for i in range(pivot_table.conditional_formats.count):
    format = pivot_table.conditional_formats[i]
    for j in range(format.format_conditions.count):
        condition = format.format_conditions[j]
        print(f"Format {i}: {condition.type} {condition.operator} formula1={condition.formula1}")
    for area in format.get_cell_areas():
        print(
            f"    rows {area.start_row + 1}-{area.end_row + 1}, "
            f"columns {area.start_column + 1}-{area.end_column + 1}"
        )
# Det här skriver ut:
# Villkorsformat: 1
# Format 0: CellValue GreaterThan formula1==200
#     rader 4-7, kolumner 6-6        (F4:F7, det lösta dataområdet)
```

## **Related Articles**
- [Applicera stil på pivottabell](/cells/sv/python-net/apply-style-to-pivot-table/)
- [Formatera del av en pivottabell](/cells/sv/python-net/format-part-of-pivot-table/)
- [Topp 10 Visa eller filtrera i pivottabell](/cells/sv/python-net/top-10-show-or-filter-in-pivot-table/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/python-net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python-net" >}}