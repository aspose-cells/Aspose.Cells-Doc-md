---
title: Formatera en del av en pivottabell
linktitle: Formatera en del av en pivottabell
description: Formatera en del av en pivottabell i Aspose.Cells for .NET genom att tillämpa stilar på semantiska PivotArea‑områden eller CellArea‑rektanglar via PivotTable.Format, med format lagrade i PivotTable.PivotFormats och bevarade när pivottabellen uppdateras.
keywords: Aspose.Cells, pivottabell, formatering, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C#
type: docs
weight: 20
url: /sv/net/format-part-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
`PivotTable.FormatAll` tillämpar en enda stil på hela pivottabellen och behandlas på föräldrasidan. Den skiljer inte mellan etiketter, värden, totaler eller specifika områden i rapporten.
I praktiken är det vanligt att bara en del av en pivottabell behöver framhävas. Vanliga mål inkluderar etiketter som tillhör ett radfält, värdeceller som produceras av ett fält, grand‑total‑raden eller en godtycklig rektangel, såsom de två första radobjekten.
Att applicera en stil direkt på kalkylbladets celler i en pivottabell är inte samma sak. Excel sparar pivottabellsformatering som semantiska `PivotArea`‑områden snarare än som vanliga cell‑stylerecord. Ett pivot‑area‑format förblir knutet till ett område, såsom ett fälts etiketter eller datavärden, och återupplöses när pivottabellen beräknas om, uppdateras eller expanderas. En stil som skrivs direkt till en cell hör däremot till den specifika cellpositionen och spåras inte av pivot‑modellen.
Aspose.Cells exponerar hela `PivotTable.Format`‑överladdningsfamiljen så att båda typerna av formatering är tillgängliga:
- `Format(PivotArea, Style)` anknyter en stil till ett semantiskt område som byggs med `PivotArea.Select` eller `PivotArea.SelectField`.
- `Format(CellArea, Style)` anknyter en stil till en kalkylbladsrektangel inom pivottabellen.
- `Format(int row, int column, Style)` riktar sig mot en enskild cell.
- `FormatAll(Style)` formaterar hela pivottabellen.

## **Formatera ett Pivot‑område**
Arbetssättet med semantiskt område är den rekommenderade metoden när en markering måste följa ett fält eller ett område i rapporten.
1. Skapa en `PivotArea` med `new PivotArea(pivotTable)`. Objektet beskriver ett semantiskt område som tillhör den specifika pivottabellen.
1. Välj ett fält efter dess nollbaserade position på en given axel med `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` väljer både fältets etiketter och data.
   - `PivotTableSelectionType.LabelOnly` väljer endast fältets etiketter.
   - `PivotTableSelectionType.DataOnly` väljer endast fältets dataceller.
1. Välj ett fält efter namn med `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. När ett radfält väljs efter namn, löses området upp till de värdeceller som produceras av fältets objekt.
1. Skapa en `Style` med `Workbook.CreateStyle()`, konfigurera dess typsnitt, förgrundsfärg och solitt bakgrundsmönster, och skicka stilen till `PivotTable.Format(area, style)`.
1. Varje anrop av `PivotArea`‑överlagringen lägger till en `PivotTableFormat`‑post i `PivotTable.PivotFormats`.
1. Fältanknutna format målas när pivotdatan beräknas. Därför bör `PivotTable.CalculateData()` anropas efter att formaten har applicerats så att stilarna blir synliga.
Följande exempel bygger en liten pivottabell för fruktförsäljning, formaterar `Fruit`‑radetiketterna med `PivotArea.Select` och `PivotTableSelectionType.LabelOnly`, formaterar värdecellerna som produceras av samma radfält med `PivotArea.SelectField`, och beräknar sedan pivottabellen på nytt så att båda stilarna målas.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Fruit sales data
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
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.CreateStyle();
labelStyle.Font.IsBold = true;
labelStyle.ForegroundColor = Color.Yellow;
labelStyle.Pattern = BackgroundType.Solid;
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.Select(PivotFieldType.Row, 0, PivotTableSelectionType.LabelOnly);
pivotTable.Format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.CreateStyle();
valueStyle.ForegroundColor = Color.LightGreen;
valueStyle.Pattern = BackgroundType.Solid;
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.SelectField(PivotFieldType.Row, "Fruit");
pivotTable.Format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.CalculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.Save("FormatPivotArea.xlsx");
```

## **Formatera ett cellområde i pivottabellen**
Använd `PivotTable.Format(CellArea, Style)` när intresseområdet är en enkel kalkylbladsrektangel snarare än ett semantiskt pivot‑område.
`CellArea` beskrivs av egenskaperna `StartRow`, `StartColumn`, `EndRow` och `EndColumn`. Värdena är nollbaserade kalkylbladskoordinater, och slutkoordinaterna identifierar den sista raden och kolumnen som ingår i rektangeln, så området täcker cellerna från startpositionen till och med slutpositionen.
Till skillnad från ett fältanknutet format appliceras ett `CellArea`‑format på cellerna omedelbart. Ett ytterligare anrop av `CalculateData()` behövs inte för att stilen ska visas.
En `CellArea`‑rektangel kan innehålla både etikettceller och värdeceller samtidigt. Nästa avsnitt beskriver hur Aspose.Cells och Excel representerar den rektangeln internt.
Följande exempel formaterar rektangeln `E4:F5` i pivottabellen med en kursiv, ljusblå stil och sparar arbetsboken utan ytterligare omberäkning.

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
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.Save("FormatPivotCellArea.xlsx");
```

## **Hur pivot‑områden och cell‑områden mappar**
Excel sparar pivottabellsformatering som `pivotArea`‑poster snarare än som vanliga kalkylbladscell‑stilposter. Samma modell används av Aspose.Cells, så en formateringsbegäran översätts till pivot‑områden när den registreras.
Relationen mellan `CellArea` som tillhandahålls av användaren och de pivot‑områden som lagras internt är många‑till‑många i båda riktningarna.
- Ett `CellArea` kan producera flera pivot‑områden. Om rektangeln omfattar både etikettceller och värdeceller delas den upp i separata etikett‑ och dataregler, eftersom pivot‑modellen behandlar etikettformatering och dataformatering oberoende av varandra.
- Ett pivot‑område kan lösa upp i flera separata `CellArea`‑instanser. Ett semantiskt område som en slutsummarad eller ett fält vars objekt inte är sammanhängande kan täcka flera rektanglar. Detta är anledningen till att `PivotArea.GetCellAreas()` returnerar en samling istället för en enda rektangel.
Varje formateringsoperation som utförs via `PivotTable.Format` registreras i `PivotTable.PivotFormats`. Varje `PivotTableFormat`‑post visar den associerade `PivotArea` och den `Style` som appliceras på den. `PivotArea`‑överlagringen lägger till exakt en post per anrop, medan ett `CellArea` som innehåller olika semantiska regioner kan lägga till flera poster.
För att skilja på de lagrade regionerna visar varje `PivotArea` flaggorna `OnlyLabel` och `OnlyData`. Exemplet nedan formaterar en enkel rektangel som täcker både etiketter och värden, undersöker `PivotTable.PivotFormats` och skriver ut `CellArea`‑koordinaterna som varje lagrat pivot‑område löser upp till.

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
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
// ONE rectangle in...
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
Console.WriteLine("Stored formats: " + pivotTable.PivotFormats.Count);
for (int i = 0; i < pivotTable.PivotFormats.Count; i++)
{
    PivotArea storedArea = pivotTable.PivotFormats[i].PivotArea;
    Console.WriteLine($"Format {i}: OnlyLabel={storedArea.OnlyLabel}, OnlyData={storedArea.OnlyData}");
    foreach (CellArea resolved in storedArea.GetCellAreas())
        Console.WriteLine($"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}");
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=True, OnlyData=False
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=False, OnlyData=True
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.Save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Eftersom formaten lagras som pivot‑områden snarare än som vanliga cellstilar, överlever de omberäkning och uppdatering. När pivottabellen uppdateras med `PivotTable.RefreshData`, beräknas om med `CalculateData`, eller sparas och läses in igen, löser varje lagrat pivot‑område upp till den aktuella positionen för sitt område och dess stil återappliceras.
{{% /alert %}}

Använd ett `PivotArea` byggt med `Select` eller `SelectField` när en markering måste förbli knuten till ett fält eller ett semantiskt område över uppdateringar, och använd ett `CellArea` när formatering av en fast rektangel i den aktuella pivottabellens layout är tillräcklig. En‑cell‑`Format(int row, int column, Style)`‑överlagring riktar sig mot en enskild cell. Använd `FormatAll`, som behandlas på föräldrasidan, när hela pivottabellen ska återformateras på en gång.

## **Related Articles**
- [Applicera stil på pivottabell](/cells/sv/net/apply-style-to-pivot-table/)
- [Lägga till rad‑ och kolumnfält i pivottabell](/cells/sv/net/pivot-table-add-row-and-column-fields/)
- [Hantera värdefält i pivottabell](/cells/sv/net/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}