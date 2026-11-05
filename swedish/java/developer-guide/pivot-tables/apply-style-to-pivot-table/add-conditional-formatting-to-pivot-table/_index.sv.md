---
title: Lägg till villkorsstyrd formatering i en pivottabell
linktitle: Lägg till villkorsstyrd formatering i en pivottabell
description: Lägg till villkorsstyrd formatering i en pivottabell i Aspose.Cells for Java - förankra en regel till dataområdet med applyTo och ett PivotConditionFormatScopeType‑område, eller definiera målet med addCellArea och getPivotAreas, och sedan bifoga regler och stilar via FormatConditions.addCondition.
keywords: Aspose.Cells for Java, pivottabell, villkorsstyrd formatering, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Java
type: docs
weight: 30
url: /sv/java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Stilarna som beskrivs på föräldrasidan och på systersidan är statiska – ett `PivotArea`‑ eller `CellArea`‑intervall färgas en gång och behåller sin stil oavsett vilka värden som finns. Villkorsstyrd formatering är den regelbaserade motsvarigheten – markera varje belopp över 200, skugga de mellersta femtio procenten, eller flagga de lägst rankade objekten – och markeringen följer värdena när pivottabellen omräknas eller uppdateras.
I Aspose.Cells finns pivottabellens villkorsstyrda formatering i samlingen `PivotTable.getConditionalFormats()`. Varje element är ett `PivotConditionalFormat` som svarar på två frågor oberoende av varandra:
- **Var gäller regeln?** Målnområdet definieras antingen via `applyTo(int row, int column, PivotConditionFormatScopeType scope)`, vilket speglar urvalet av område i Excel‑gränssnittet, eller via `addCellArea(CellArea)` och samlingen `getPivotAreas()`, som namnger området explicit.
- **Vad testar regeln?** En eller flera villkor läggs till i `getFormatConditions()` med `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, och varje villkor har sin egen `Style`.

{{% alert color="primary" %}}
Anropa inte `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` eller `FormatConditionCollection.addArea(CellArea)` på `getFormatConditions()`‑samlingen för ett pivottabells villkorsstyrda format. Dessa två överlagringar är ärvda från den vanliga kalkylblads‑API:n för villkorsstyrd formatering och fungerar inte för pivottabeller – cellområdet konverteras aldrig till ett pivottabell‑område, så begäran ignoreras tyst. Definiera alltid området på själva `PivotConditionalFormat` (`applyTo`, `addCellArea` eller `getPivotAreas()`) och lägg till regeln med någon av `addCondition`‑överlagringarna.
{{% /alert %}}

## **Applicera en regel med ett område (Excel‑gränssnittet)**
Det första sättet placerar regeln på samma sätt som Excel‑gränssnittet. En cell i pivottabellen namnges med sina nollbaserade kalkylbladskoordinater, och ett `PivotConditionFormatScopeType`‑område talar om för Aspose.Cells hur långt regeln ska sträcka sig från den cellen:
- `PivotConditionFormatScopeType.DATA` – alla värdeceller som pivottabellen producerar, inklusive totalsummor.
- `PivotConditionFormatScopeType.FIELD` – de värdeceller som tillhör det fält som cellen identifierar, exklusive totalsummor. Cellen måste vara en fältcell, t.ex. en rad‑fälttitel; att skicka en värdecell ger ett undantag.
- `PivotConditionFormatScopeType.SELECTION` – endast de värdeceller i skärningspunkten som cellen väljer, vanligtvis en enda värdecell.
Exemplet nedan bygger en pivottabell för fruktförsäljning med övre vänstra hörnet i E3, förankrar ett villkorsstyrt format i cellen F4 (rad 3, kolumn 5) med `DATA`‑området, och markerar varje belopp över 200 med fet vit på röd. Med värdena Apple 220, Banana 330, Cherry 200 och totalsumman 750 färgar regeln F4, F5 och F7 – det lösta området är hela datakolumnen F4:F7, och endast de celler vars värde uppfyller regeln lyser upp.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot‑tabell med dess övre vänstra hörn på E3
PivotTable pivotTable = sheet.getPivotTables().add("A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Fäst det villkorliga formatet på F4 (rad 3, kolumn 5) med data‑omfånget
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA);
// Regel – markera belopp som är större än 200
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.GREATER_THAN, "200", null);
Style style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(Color.getWhite());
style.setForegroundColor(Color.getRed());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Att förankra samma regel vid rad‑fälttiteln E4 (rad 3, kolumn 4) med `FIELD`‑området löser till F4:F6 istället – samma datakolumn utan totalsummarraden – eftersom området nu beskriver fältet `Fruit` snarare än hela värdeområdet. `SELECTION`‑området som förankras i F4 löser endast till F4.

## **Definiera området manuellt**
Det andra sättet hoppar över område‑urvalet och namnger området explicit på `PivotConditionalFormat`.

### **Ett kalkylbladsrektangel med addCellArea**
`addCellArea(CellArea)` registrerar den givna rektangeln som mål för regeln. Koordinaterna är nollbaserade kalkylbladskoordinater, och området är exakt den levererade rektangeln – ingen expansion till datakolumnen och ingen totalsummalogik. Använd detta när de intressanta cellerna är en känd fast rektangel i det aktuella pivottabellens layout.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Markera rektangeln F4:F6 (värdecellerna utan totalen)
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
CellArea cellArea = new CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Regel - kursiv på ljusgul för belopp mellan 150 och 300
int conditionIndex = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300");
Style style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(Color.getLightYellow());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Ett semantiskt pivottabellsområde med getPivotAreas**
`getPivotAreas()` returnerar samma semantiska‑områdesmodell som systersidan använder för statiska stilar. Skapa ett `PivotArea`, välj ett fält eller område med `select` eller `selectField`, och lägg till det med `getPivotAreas().addPivotArea(PivotArea)`. Ett semantiskt område förblir kopplat till sitt fält, så den villkorsstyrda formateringen följer fältet när pivottabellen uppdateras och layouten förändras. Överlagringen `getPivotAreas().add(PivotArea)` kompilerar fortfarande men är markerad som föråldrad – föredra `addPivotArea`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Fäst regeln på datakolumnen Amount som ett semantiskt område
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
PivotArea area = new PivotArea(pivotTable);
area.selectField(PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Regel - grå text för belopp under 150
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.LESS_THAN, "150", null);
Style style = workbook.createStyle();
style.getFont().setColor(Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Var reglerna lagras och hur de överlever en omladdning**
Varje anrop till `getConditionalFormats().add()` lägger till ett `PivotConditionalFormat` i pivottabellen. Villkoren, deras formler och deras stilar sparas med arbetsboken – när filen öppnas igen i exemplen nedan visas samma regel med sin typ, operator och formel intakt, och `getCellAreas()` rapporterar samma områden. Poster som aldrig fick ett villkor tas bort när arbetsboken sparas, på samma sätt som Excel kastar en villkorsstyrd formatering utan regel.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
System.out.println("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (int i = 0; i < pivotTable.getConditionalFormats().getCount(); i++)
{
    PivotConditionalFormat format = pivotTable.getConditionalFormats().get(i);
    for (int j = 0; j < format.getFormatConditions().getCount(); j++)
    {
        FormatCondition condition = format.getFormatConditions().get(j);
        System.out.println("Format " + i + ": " + condition.getType() + " " + condition.getOperator() + " formula1=" + condition.getFormula1());
    }
    for (CellArea area : format.getCellAreas())
    {
        System.out.println("    rows " + (area.StartRow + 1) + "-" + (area.EndRow + 1)
                + ", columns " + (area.StartColumn + 1) + "-" + (area.EndColumn + 1));
    }
}
// Detta skriver ut:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rader 4-7, kolumner 6-6        (F4:F7, det lösta dataområdet)
```

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/java/apply-style-to-pivot-table/)
- [Formatera del av en pivottabell](/cells/sv/java/format-part-of-pivot-table/)
- [Topp‑10 Visa eller filtrera i pivottabell](/cells/sv/java/top-10-show-or-filter-in-pivot-table/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="java" >}}