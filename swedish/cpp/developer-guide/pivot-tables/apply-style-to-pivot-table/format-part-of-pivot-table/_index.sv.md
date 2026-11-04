---
title: Formatera del av en pivottabell
linktitle: Formatera del av en pivottabell
description: Formatera del av en pivottabell i Aspose.Cells för C++ genom att tillämpa stilar på semantiska PivotArea‑områden eller CellArea‑rektanglar via PivotTable.Format, med format lagrade i PivotTable.GetPivotFormats och bevarade när pivottabellen uppdateras.
keywords: Aspose.Cells, pivottabell, format, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /sv/cpp/format-part-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
`PivotTable.FormatAll` tillämpar en enda stil på hela pivottabellen och behandlas på föräldrasidan. Den skiljer inte mellan etiketter, värden, totaler eller specifika områden i rapporten.  
I praktiken behöver endast en del av en pivottabell vanligtvis framträda. Vanliga mål inkluderar etiketterna som tillhör ett radfält, värdecellerna som produceras av ett fält, totalraden eller en godtycklig rektangel såsom de två första postraderna.  
Att tillämpa en stil direkt på kalkylbladets celler i en pivottabell är inte ekvivalent. Excel lagrar pivottabellformat som semantiska `PivotArea`‑områden snarare än som vanliga cell‑stilregister. Ett pivot‑områdeformat förblir knutet till ett område såsom ett fälts etiketter eller datavärden, och det löses om när pivottabellen beräknas om, uppdateras eller expanderas. En stil som skrivs direkt till en cell tillhör däremot den specifika cellpositionen och spåras inte av pivot‑modellen.  
Aspose.Cells exponerar den kompletta överlagringsfamiljen `PivotTable.Format` så att båda typerna av formatering är tillgängliga:
- `Format(const PivotArea&, const Style&)` fäster en stil på ett semantiskt område som byggs med `PivotArea.Select` eller `PivotArea.SelectField`.
- `Format(const CellArea&, const Style&)` fäster en stil på en kalkylbladsrektangel inuti pivottabellen.
- `Format(int32_t row, int32_t column, const Style&)` riktar in sig på en enskild cell.
- `FormatAll(const Style&)` formaterar hela pivottabellen.

## **Formatera ett Pivot‑område**
Det semantiska arbetsflödet med områden är den rekommenderade metoden när en markering måste följa ett fält eller ett område i rapporten.
1. Skapa ett `PivotArea` med `PivotArea pivotArea(pivotTable);`. Objektet beskriver ett semantiskt område som tillhör just den pivottabellen.  
1. Välj ett fält efter dess nollbaserade position på en given axel med `PivotArea.Select(PivotFieldType axisType, int32_t fieldPosition, PivotTableSelectionType selectionType)`.  
   - `PivotTableSelectionType::DataAndLabel` väljer både etiketter och data för fältet.  
   - `PivotTableSelectionType::LabelOnly` väljer endast fältets etiketter.  
   - `PivotTableSelectionType::DataOnly` väljer endast fältets dataceller.  
1. Välj ett fält efter namn med `PivotArea.SelectField(PivotFieldType axisType, const char16_t* fieldName)`. När ett radfält väljs efter namn, löser området upp till de värdeceller som produceras av fältets objekt.  
1. Skapa ett `Style` med `Workbook.CreateStyle()`, konfigurera dess teckensnitt, förgrundsfärg och solid bakgrundsmönster, och skicka stilen till `PivotTable.Format(pivotArea, style)`.  
1. Varje anrop till `PivotArea`‑överlagringen lägger till ett `PivotTableFormat`‑objekt i `PivotTable.GetPivotFormats()`.  
1. Fält‑ankrade format målas när pivotdatan beräknas. Anropa därför `PivotTable.CalculateData()` efter att formaten har tillämpats så att stilarna blir synliga.  
Följande exempel bygger en liten pivottabell för fruktförsäljning, formaterar radetiketterna för `Fruit` med `PivotArea.Select` och `PivotTableSelectionType::LabelOnly`, formaterar värdecellerna som produceras av samma radfält med `PivotArea.SelectField` och beräknar sedan pivottabellen på nytt så att båda stilarna målas.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Fruit sales data
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Pivot table with its top-left corner at E3
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Bold yellow fill on the row field's label cells
    Style labelStyle = workbook.CreateStyle();
    labelStyle.GetFont().SetIsBold(true);
    labelStyle.SetForegroundColor(Color::Yellow());
    labelStyle.SetPattern(BackgroundType::Solid);
    PivotArea labelArea(pivotTable);
    labelArea.Select(PivotFieldType::Row, 0, PivotTableSelectionType::LabelOnly);
    pivotTable.Format(labelArea, labelStyle);
    // Light green fill on the value cells the row field produces
    Style valueStyle = workbook.CreateStyle();
    valueStyle.SetForegroundColor(Color::LightGreen());
    valueStyle.SetPattern(BackgroundType::Solid);
    PivotArea valueArea(pivotTable);
    valueArea.SelectField(PivotFieldType::Row, u"Fruit");
    pivotTable.Format(valueArea, valueStyle);
    // Field-anchored formats are painted when the data is calculated
    pivotTable.CalculateData();
    // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
    workbook.Save(u"FormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Formatera ett Cell‑område i pivottabellen**
Använd `PivotTable.Format(const CellArea&, const Style&)` när intresseområdet är en enkel kalkylbladsrektangel snarare än ett semantiskt pivot‑område.  
Ett `CellArea` beskrivs av de offentliga fälten `StartRow`, `StartColumn`, `EndRow` och `EndColumn`. Värdena är nollbaserade kalkylbladskoordinater, och slutkoordinaterna identifierar den sista raden och kolumnen som ingår i rektangeln, så området omfattar cellerna från startpositionen till slutpositionen inklusivt.  
Till skillnad från ett fält‑ankrat format appliceras ett `CellArea`‑format omedelbart på cellerna. Ett ytterligare anrop till `CalculateData()` behövs inte för att stilen ska visas.  
Ett `CellArea`‑rektangel kan innehålla både etikett‑celler och värde‑celler. Nästa avsnitt beskriver hur Aspose.Cells och Excel representerar den rektangeln internt.  
Följande exempel formaterar rektangeln `E4:F5` i pivottabellen med en kursiv, ljusblå stil och sparar arbetsboken utan någon ytterligare omberäkning.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Highlight the first two fruit rows (the rectangle E4:F5)
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // E4:F5 is italic on light blue immediately, no recalculation needed
    workbook.Save(u"FormatPivotCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Hur Pivot‑områden och Cell‑områden kartläggs**
Excel lagrar pivottabellformat som `pivotArea`‑poster snarare än som vanliga kalkylblads‑cell‑stilposter. Samma modell används av Aspose.Cells, så en formateringsbegäran översätts till pivot‑områden när den registreras.  
Relationen mellan det `CellArea` som användaren tillhandahåller och de pivot‑områden som lagras internt är många‑till‑många i båda riktningarna.
- Ett `CellArea` kan generera flera pivot‑områden. Om rektangeln sträcker sig över både etikett‑celler och värde‑celler, delas den upp i separata etikett‑ och dataregler, eftersom pivot‑modellen behandlar etikett‑format och data‑format oberoende av varandra.
- Ett pivot‑område kan lösa upp till flera skilda `CellArea`‑instanser. Ett semantiskt område såsom en totalrad, eller ett fält vars objekt inte är sammanhängande, kan täcka flera rektanglar. Detta är anledningen till att `PivotArea.GetCellAreas()` returnerar en `Vector<CellArea>` istället för en enda rektangel.
Varje formatoperation som utförs via `PivotTable.Format` registreras i `PivotTable.GetPivotFormats()`. Varje `PivotTableFormat`‑post exponerar den associerade `PivotArea` och den `Style` som appliceras på den. `PivotArea`‑överlagringen lägger exakt till ett objekt per anrop, medan ett `CellArea` som innehåller olika semantiska regioner kan lägga till flera poster.  
För att skilja på de lagrade regionerna exponerar varje `PivotArea` flaggorna `GetOnlyLabel()` och `GetOnlyData()`. Exemplet nedan formaterar en enda rektangel som täcker både etiketter och värden, inspekterar `PivotTable.GetPivotFormats()` och skriver ut `CellArea`‑koordinaterna som varje lagrat pivot‑område löser upp till.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    // ONE rectangle in...
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // ...TWO semantic pivot areas out: the label part and the data part are stored separately
    std::cout << "Stored formats: " << pivotTable.GetPivotFormats().GetCount() << std::endl;
    for (int i = 0; i < pivotTable.GetPivotFormats().GetCount(); i++)
    {
        PivotArea storedArea = pivotTable.GetPivotFormats().Get(i).GetPivotArea();
        std::cout << "Format " << i << ": OnlyLabel=" << (storedArea.GetOnlyLabel() ? "true" : "false")
                  << ", OnlyData=" << (storedArea.GetOnlyData() ? "true" : "false") << std::endl;
        Vector<CellArea> resolved = storedArea.GetCellAreas();
        for (int j = 0; j < resolved.GetLength(); j++)
        {
            std::cout << "    rows " << (resolved[j].StartRow + 1) << "-" << (resolved[j].EndRow + 1)
                      << ", columns " << (resolved[j].StartColumn + 1) << "-" << (resolved[j].EndColumn + 1) << std::endl;
        }
    }
    // This prints:
    // Stored formats: 2
    // Format 0: OnlyLabel=true, OnlyData=false
    //     rows 4-5, columns 5-5        (E4:E5, the label part)
    // Format 1: OnlyLabel=false, OnlyData=true
    //     rows 4-5, columns 6-6        (F4:F5, the data part)
    workbook.Save(u"FormatPivotAreasMap.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
Eftersom formaten lagras som pivot‑områden snarare än som vanliga cellstilar, överlever de omberäkning och uppdatering. När pivottabellen uppdateras med `PivotTable.RefreshData`, beräknas om med `CalculateData`, eller sparas och laddas om, löser varje lagrat pivot‑område upp till den aktuella positionen för sitt område och dess stil appliceras igen.
{{% /alert %}}

Använd ett `PivotArea` byggt med `Select` eller `SelectField` när en markering måste förbli knuten till ett fält eller ett semantiskt område över uppdateringar, och använd ett `CellArea` när formatering av en fast rektangel i den aktuella pivottabellslayouten är tillräcklig. Den enstaka cell‑överlagringen `Format(int32_t row, int32_t column, const Style&)` riktar in sig på en individuell cell. Använd `FormatAll`, som behandlas på föräldrasidan, när hela pivottabellen bör omformateras på en gång.

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/cpp/apply-style-to-pivot-table/)
- [Lägga till rader och kolumner i pivottabell](/cells/sv/cpp/pivot-table-add-row-and-column-fields/)
- [Hantera värdefält i pivottabell](/cells/sv/cpp/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}