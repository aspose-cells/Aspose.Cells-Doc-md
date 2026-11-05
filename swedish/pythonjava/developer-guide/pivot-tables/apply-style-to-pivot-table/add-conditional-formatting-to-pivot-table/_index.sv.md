---
title: Lägg till villkorsstyrd formatering i en pivottabell
linktitle: Lägg till villkorsstyrd formatering i en pivottabell
description: Lägg till villkorsstyrd formatering i en pivottabell i Aspose.Cells for Python via Java, ankra en regel till dataområdet med applyTo och en PivotConditionFormatScopeType‑omfång, eller definiera målet med addCellArea och getPivotAreas, och sedan bifoga regler och stilar via getFormatConditions().addCondition.
keywords: Aspose.Cells for Python via Java, pivottabell, villkorsstyrd formatering, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Python via Java
type: docs
weight: 30
url: /sv/python-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Stilarna som beskrivs på föräldrasidan och på sidorna bredvid är statiska – ett `PivotArea`‑ eller `CellArea`‑område färgas en gång och behåller sin stil oavsett vilka värden som finns. Villkorsstyrd formatering är den regelbaserade motsvarigheten – markera varje belopp över 200, skugga de mittersta femtio procenten, eller flagga de längst ner rankade objekten – och markeringen följer värdena varje gång pivottabellen beräknas om eller uppdateras.  
I Aspose.Cells lagras pivottabellens villkorsstyrda formatering i samlingen `PivotTable.getConditionalFormats()`. Varje post är ett `PivotConditionalFormat` som svarar på två frågor oberoende av varandra:
- **Var tillämpas regeln?** Målet definieras antingen via `PivotConditionalFormat.applyTo(int row, int column, PivotConditionFormatScopeType scope)`, vilket speglar omfångsväljaren i Excel‑användargränssnittet, eller via `PivotConditionalFormat.addCellArea(CellArea)` och samlingen `PivotConditionalFormat.getPivotAreas()`, som explicit namnger området.
- **Vad testar regeln?** En eller flera villkor läggs till i `PivotConditionalFormat.getFormatConditions()` med `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, och varje villkor bär sin egen `Style`.

{{% alert color="primary" %}}
Anropa inte `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` eller `FormatConditionCollection.addArea(CellArea)` på objektet `PivotConditionalFormat.getFormatConditions()` för ett villkorligt pivottabellformat. Dessa två överlagringar är ärvda från det vanliga kalkylbladets villkorsstyrda formaterings‑API och fungerar inte för pivottabeller – cellområdet konverteras aldrig till ett pivotområde, så förfrågan ignoreras tyst. Definiera alltid området på själva `PivotConditionalFormat` (`applyTo`, `addCellArea` eller `getPivotAreas()`) och lägg till regeln med en av `addCondition`‑överlagringarna.
{{% /alert %}}

## **Tillämpa en regel med ett omfång (Excel‑gränssnittet)**
Det första sättet placerar regeln på samma sätt som Excel‑användargränssnittet gör. En cell i pivottabellen namnges av dess nollbaserade kalkylbladskoordinater, och ett `PivotConditionFormatScopeType`‑omfång talar om för Aspose.Cells hur långt regeln ska sträcka sig från den cellen:
- `PivotConditionFormatScopeType.DATA` – alla värdeceller som pivottabellen producerar, inklusive totalsummor.
- `PivotConditionFormatScopeType.FIELD` – de värdeceller som tillhör fältet som cellen identifierar, exklusive totalsummor. Cellen måste vara en fältcell, t.ex. en rad‑fältetikett; att skicka en värdecelle kastar ett undantag.
- `PivotConditionFormatScopeType.SELECTION` – endast de värdeceller i den skärningspunkt som cellen väljer, vanligtvis en enda värdecell.
Exemplet nedan bygger en frukt‑försäljnings‑pivottabell med sitt övre‑vänstra hörn i E3, ankralägger ett villkorsformat på cell F4 (rad 3, kolumn 5) med `DATA`‑omfånget, och markerar varje belopp större än 200 med fet vit text på röd bakgrund. Med värdena Apple 220, Banana 330, Cherry 200 och totalsumman 750 målar regeln F4, F5 och F7 – det lösta området är hela datakolumnen F4:F7, och endast de celler vars värde uppfyller regeln lyser upp.

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
    PivotFieldType,
    PivotConditionFormatScopeType,
    FormatConditionType,
    OperatorType,
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
# Pivot-tabell med dess övre vänstra hörn i E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Anknyta det villkorliga formatet vid F4 (rad 3, kolumn 5) med Data-omfånget
index = pivot_table.getConditionalFormats().add()
format = pivot_table.getConditionalFormats().get(index)
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA)
# Regel - markera belopp större än 200
condition_index = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.GREATER_THAN,
    "200",
    None,
)
style = workbook.createStyle()
style.getFont().setBold(True)
style.getFont().setColor(Color.getWhite())
style.setForegroundColor(Color.getRed())
style.setPattern(BackgroundType.SOLID)
format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatData.xlsx")
jpype.shutdownJVM()
```

Att ankra samma regel på rad‑fältetiketten E4 (rad 3, kolumn 4) med `FIELD`‑omfånget ger området F4:F6 istället – samma datakolumn utan totalsummoraden – eftersom omfånget nu beskriver `Fruit`‑fältet snarare än hela värdeområdet. `SELECTION`‑omfånget som ankras på F4 löser endast upp F4.

## **Definiera området manuellt**
Det andra sättet hoppar över omfångsväljaren och namnger området explicit på `PivotConditionalFormat`.

### **Ett kalkylbladsrektangel med addCellArea()**
`addCellArea(CellArea)` registrerar den angivna rektangeln som mål för regeln. Koordinaterna är nollbaserade kalkylbladskoordinater, och området är exakt den rektangel som levereras – ingen expansion till datakolumnen och ingen totalsummelogik. Använd detta när de intressanta cellerna är en känd fast rektangel i den aktuella pivottabellslayouten.

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
    CellArea,
    Color,
    BackgroundType,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
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
# Rikta in rektangeln F4:F6 (värdecellerna utan totalen)
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = CellArea()
area.StartRow = 3
area.StartColumn = 5
area.EndRow = 5
area.EndColumn = 5
conditional_format.addCellArea(area)
# Regel - kursiv på ljusgul för belopp mellan 150 och 300
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.BETWEEN,
    "150",
    "300",
)
style = workbook.createStyle()
style.getFont().setItalic(True)
style.setForegroundColor(Color.getLightYellow())
style.setPattern(BackgroundType.SOLID)
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatCellArea.xlsx")
jpype.shutdownJVM()
```

### **Ett semantiskt PivotArea med getPivotAreas()**
Samlingen `getPivotAreas()` är samma semantiska‑områdesmodell som sidan bredvid använder för statiska stilar. Bygg ett `PivotArea`, välj ett fält eller område med `PivotArea.select(...)` eller `PivotArea.selectField(...)`, och lägg till det med `getPivotAreas().addPivotArea(PivotArea)`. Ett semantiskt område förblir knutet till sitt fält, så det villkorsstyrda formatet följer fältet när pivottabellen uppdateras och layouten förändras. Överlagringen `getPivotAreas().add(PivotArea)` kompilerar fortfarande men är markerad som föråldrad – föredra `addPivotArea`.

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
    PivotArea,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
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
# Bifoga regeln till datafältet Amount som ett semantiskt område
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = PivotArea(pivot_table)
area.selectField(PivotFieldType.DATA, "Amount")
conditional_format.getPivotAreas().addPivotArea(area)
# Regel - grå text för belopp under 150
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.LESS_THAN,
    "150",
    None,
)
style = workbook.createStyle()
style.getFont().setColor(Color.getGray())
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Var reglerna lagras och hur de överlever en omläsning**
Varje anrop `PivotTable.getConditionalFormats().add()` lägger till ett `PivotConditionalFormat` i pivottabellen. Villkoren, deras formler och deras stilar sparas med arbetsboken – att öppna filen igen i exemplet nedan visar samma regel med sin typ, operator och formel intakt, och `PivotConditionalFormat.getCellAreas()` rapporterar samma områden. Poster som aldrig fick ett villkor tas bort när arbetsboken sparas, på samma sätt som Excel bortser från ett villkorsformat som saknar regel.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
print("Conditional formats: " + str(pivot_table.getConditionalFormats().getCount()))
for i in range(pivot_table.getConditionalFormats().getCount()):
    pivot_format = pivot_table.getConditionalFormats().get(i)
    format_conditions = pivot_format.getFormatConditions()
    for j in range(format_conditions.getCount()):
        condition = format_conditions.get(j)
        print(
            f"Format {i}: {condition.getType()} "
            f"{condition.getOperator()} formula1={condition.getFormula1()}"
        )
    for area in pivot_format.getCellAreas():
        print(
            f"    rows {area.StartRow + 1}-{area.EndRow + 1}, "
            f"columns {area.StartColumn + 1}-{area.EndColumn + 1}"
        )
# Detta skriver ut:
# Villkorsformat: 1
# Format 0: CellValue GreaterThan formula1==200
#     rader 4-7, kolumner 6-6        (F4:F7, den lösta datoregionen)
jpype.shutdownJVM()
```

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/python-java/apply-style-to-pivot-table/)
- [Formatera del av pivottabell](/cells/sv/python-java/format-part-of-pivot-table/)
- [Top 10 visa eller filtrera i pivottabell](/cells/sv/python-java/top-10-show-or-filter-in-pivot-table/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/python-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python" >}}