---
title: Lägg till villkorsstyrd formatering i en pivottabell
linktitle: Lägg till villkorsstyrd formatering i en pivottabell
description: Lägg till villkorsstyrd formatering i en pivottabell i Aspose.Cells för .NET, ankra en regel till dataregionen med ApplyTo och en PivotConditionFormatScopeType-omfång, eller definiera målet med AddCellArea och PivotAreas, och sedan fästa regler och stilar via FormatConditions.AddCondition.
keywords: Aspose.Cells, pivottabell, villkorsstyrd formatering, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C#
type: docs
weight: 30
url: /sv/net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Stilarna som beskrivs på föräldrasidan och på syskonsidan är statiska – ett `PivotArea`‑ eller `CellArea`‑område målas en gång och behåller sin stil oavsett vilka värden som finns. Villkorsstyrd formatering är den regelbaserade motsvarigheten – markera varje belopp över 200, skugga de mittersta femtio procenten, eller flagga de lägst rankade posterna – och markeringen följer värdena när pivottabellen beräknas om eller uppdateras.
I Aspose.Cells finns villkorsstyrd formatering för pivottabeller i samlingen `PivotTable.ConditionalFormats`. Varje post är ett `PivotConditionalFormat` som besvarar två frågor oberoende av varandra:
- **Var gäller regeln?** Målområdet definieras antingen via `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, vilket speglar områdeväljaren i Excel‑gränssnittet, eller via `AddCellArea(CellArea)` och samlingen `PivotAreas`, som namnger området explicit.
- **Vad testar regeln?** En eller flera villkor läggs till i `FormatConditions` med `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`, och varje villkor har sin egen `Style`.

{{% alert color="primary" %}}
Anropa inte `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` eller `FormatConditionCollection.AddArea(CellArea)` på `FormatConditions`‑objektet för ett pivottabell‑villkorsformat. Dessa två overloadar ärvs från det vanliga kalkylblads‑API:t för villkorsstyrd formatering och fungerar inte för pivottabeller – cellområdet konverteras aldrig till ett pivot‑område, så begäran ignoreras tyst. Definera alltid området på själva `PivotConditionalFormat` (`ApplyTo`, `AddCellArea` eller `PivotAreas`) och lägg till regeln med någon av `AddCondition`‑overloadsen.
{{% /alert %}}

## **Använd en regel med ett område (Excel‑gränssnittet)**
Det första sättet placerar regeln på samma sätt som Excel‑gränssnittet. En cell i pivottabellen identifieras med sina nollbaserade kalkylbladskoordinater, och ett `PivotConditionFormatScopeType`‑område talar om för Aspose.Cells hur långt regeln ska sträcka sig från den cellen:
- `PivotConditionFormatScopeType.Data` – alla värdeceller som pivottabellen producerar, inklusive totalrader.
- `PivotConditionFormatScopeType.Field` – de värdeceller som tillhör fältet som cellen identifierar, exklusive totalrader. Cellen måste vara en fältcell, t.ex. en rad‑fältetikett; att skicka en värdecell ger ett undantag.
- `PivotConditionFormatScopeType.Selection` – endast de värdeceller i skärningspunkten som cellen väljer, vanligtvis en enda värdecell.
Exemplet nedan bygger en pivottabell för fruktförsäljning med övre vänstra hörnet i E3, ankrar ett villkorsformat på cell F4 (rad 3, kolumn 5) med `Data`‑omfånget, och markerar varje belopp över 200 med fet vit text på röd bakgrund. Med värdena Apple 220, Banana 330, Cherry 200 och totalen 750, färgar regeln F4, F5 och F7 – det lösta området är hela datakolumnen F4:F7, och endast de celler vars värde uppfyller regeln lyser upp.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
// Pivottabell med dess övre vänstra hörn i E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Fäst det villkorsstyrda formatet på F4 (rad 3, kolumn 5) med Data-omfånget
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.ApplyTo(3, 5, PivotConditionFormatScopeType.Data);
// Regel - markera belopp som är större än 200
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
Style style = workbook.CreateStyle();
style.Font.IsBold = true;
style.Font.Color = Color.White;
style.ForegroundColor = Color.Red;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatData.xlsx");
```

Att ankra samma regel på rad‑fältetiketten E4 (rad 3, kolumn 4) med `Field`‑omfånget löser till F4:F6 istället – samma datakolumn utan totalraden – eftersom omfånget nu beskriver `Fruit`‑fältet snarare än hela värdeområdet. `Selection`‑omfånget som ankras på F4 löser endast till F4.

## **Definiera området manuellt**
Det andra sättet hoppar över områdeväljaren och namnger området explicit på `PivotConditionalFormat`.

### **Ett kalkylbladsrektangel med AddCellArea**
`AddCellArea(CellArea)` registrerar den angivna rektangeln som regelns mål. Koordinaterna är nollbaserade kalkylbladskoordinater, och området är exakt den levererade rektangeln – ingen utvidgning till datakolumnen och ingen totallogik. Använd den när de intressanta cellerna är en känd fast rektangel i den aktuella pivottabellslayouten.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Måla området F4:F6 (värdecellerna utan totalsumman)
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.AddCellArea(new CellArea { StartRow = 3, StartColumn = 5, EndRow = 5, EndColumn = 5 });
// Regel - kursiv på ljusgul för belopp mellan 150 och 300
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.Between, "150", "300");
Style style = workbook.CreateStyle();
style.Font.IsItalic = true;
style.ForegroundColor = Color.LightYellow;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatCellArea.xlsx");
```

### **Ett semantiskt pivot‑område med PivotAreas**
`PivotAreas` är samma semantiska‑områdesmodell som syskonsidan använder för statiska stilar. Bygg ett `PivotArea`, välj ett fält eller område med `Select` eller `SelectField`, och lägg till det med `PivotAreas.AddPivotArea(PivotArea)`. Ett semantiskt område förblir fäst vid sitt fält, så den villkorsstyrda formateringen följer fältet när pivottabellen uppdateras och layouten ändras. Overloaden `PivotAreas.Add(PivotArea)` kompileras fortfarande men är markerad som föråldrad – föredra `AddPivotArea`.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Fäst regeln på datatfältet Amount som ett semantiskt område
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
PivotArea area = new PivotArea(pivotTable);
area.SelectField(PivotFieldType.Data, "Amount");
format.PivotAreas.AddPivotArea(area);
// Regel - grå text för belopp under 150
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
Style style = workbook.CreateStyle();
style.Font.Color = Color.Gray;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatPivotArea.xlsx");
```

## **Var reglerna lagras och hur de överlever en omladdning**
Varje anrop till `ConditionalFormats.Add()` lägger till ett `PivotConditionalFormat` i pivottabellen. Villkoren, deras formler och deras stilar sparas tillsammans med arbetsboken – att öppna filen igen i exemplet nedan visar samma regel med sin typ, operator och formel intakt, och `GetCellAreas()` rapporterar samma områden. Poster som aldrig fått ett villkor tas bort när arbetsboken sparas, på samma sätt som Excel förkastar en villkorsformat som saknar regel.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
Console.WriteLine("Conditional formats: " + pivotTable.ConditionalFormats.Count);
for (int i = 0; i < pivotTable.ConditionalFormats.Count; i++)
{
    PivotConditionalFormat format = pivotTable.ConditionalFormats[i];
    for (int j = 0; j < format.FormatConditions.Count; j++)
    {
        FormatCondition condition = format.FormatConditions[j];
        Console.WriteLine($"Format {i}: {condition.Type} {condition.Operator} formula1={condition.Formula1}");
    }
    foreach (CellArea area in format.GetCellAreas())
        Console.WriteLine($"    rows {area.StartRow + 1}-{area.EndRow + 1}, columns {area.StartColumn + 1}-{area.EndColumn + 1}");
}
// Detta skriver ut:
// Villkorliga format: 1
// Format 0: CellValue GreaterThan formula1==200
//     rader 4-7, kolumner 6-6        (F4:F7, det lösta dataområdet)
```

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/net/apply-style-to-pivot-table/)
- [Formatera del av en pivottabell](/cells/sv/net/format-part-of-pivot-table/)
- [Topp 10 Visa eller filtrera i pivottabell](/cells/sv/net/top-10-show-or-filter-in-pivot-table/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="csharp" >}}