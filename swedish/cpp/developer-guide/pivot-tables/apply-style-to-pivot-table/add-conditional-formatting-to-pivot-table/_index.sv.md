---
title: Lägg till villkorsstyrd formatering i en pivottabell
linktitle: Lägg till villkorsstyrd formatering i en pivottabell
description: Lägg till villkorsstyrd formatering i en pivottabell i Aspose.Cells for C++ - förankra en regel till dataområdet med ApplyTo och en PivotConditionFormatScopeType-scope, eller definiera målområdet med AddCellArea och PivotAreas, och sedan bifoga regler och stilar via FormatConditions.AddCondition.
keywords: Aspose.Cells for C++, pivottabell, villkorsstyrd formatering, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /sv/cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Stilarna som beskrivs på föräldrasidan och på syskonsidan är statiska – ett `PivotArea`‑ eller `CellArea`‑område målas en gång och behåller sin stil oavsett vilka värden som finns. Villkorsstyrd formatering är den regelbaserade motsvarigheten – markera varje belopp över 200, skugga de mittersta femtio procenten, eller flagga de lägst rankade objekten – och markeringen följer värdena varje gång pivottabellen beräknas om eller uppdateras.
I Aspose.Cells finns villkorsstyrd formatering för pivottabeller i samlingen `pivotTable.GetConditionalFormats()`. Varje post är ett `PivotConditionalFormat` som besvarar två frågor oberoende:
- **Var gäller regeln?** Målområdet definieras antingen via `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, vilket speglar områdeväljaren i Excel‑användargränssnittet, eller via `AddCellArea(CellArea)` och samlingen `GetPivotAreas()`, som namnger området explicit.
- **Vad testar regeln?** En eller flera villkor läggs till via `GetFormatConditions()` med `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, och varje villkor har sin egen `Style`.

{{% alert color="primary" %}}
Anropa inte `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` eller `FormatConditionCollection.AddArea(CellArea)` på `GetFormatConditions()`‑objektet för ett pivottabell‑villkorsformat. Dessa två överlagringar ärvs från den vanliga kalkylblads‑API:et för villkorsstyrd formatering och fungerar inte för pivottabeller – cellområdet konverteras aldrig till ett pivot‑område, så förfrågan ignoreras tyst. Definiera alltid området på själva `PivotConditionalFormat` (`ApplyTo`, `AddCellArea` eller `GetPivotAreas()`) och lägg till regeln med en av `AddCondition`‑överlagringarna.
{{% /alert %}}

## **Applicera en regel med ett omfång (Excel‑gränssnittet)**
Det första sättet placerar regeln på samma sätt som Excel‑användargränssnittet gör. En cell i pivottabellen namnges av dess nollbaserade kalkylbladskoordinater, och ett `PivotConditionFormatScopeType`‑omfång talar om för Aspose.Cells hur långt regeln ska sträcka sig från den cellen:
- `PivotConditionFormatScopeType::Data` – alla värdeceller som pivottabellen producerar, inklusive totalsummor.
- `PivotConditionFormatScopeType::Field` – de värdeceller som tillhör det fält som cellen identifierar, exklusive totalsummor. Cellen måste vara en fältcell, t.ex. en rad‑fältetikett; att skicka en värdecell kastar ett undantag.
- `PivotConditionFormatScopeType::Selection` – endast de värdeceller som är i skärningspunkten som cellen väljer, vanligtvis en enda värdecell.
Exemplet nedan bygger en pivottabell för fruktförsäljning vars övre vänstra hörn är på E3, förankrar ett villkorsformat på cell F4 (rad 3, kolumn 5) med `Data`‑omfånget, och markerar varje belopp över 200 med fet vit text på röd bakgrund. Med värdena Apple 220, Banana 330, Cherry 200 och totalsumman 750, målar regeln F4, F5 och F7 – det lösta området är hela datakolumnen F4:F7, och endast de celler vars värde uppfyller regeln lyser upp.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    format.ApplyTo(3, 5, PivotConditionFormatScopeType::Data);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::GreaterThan, u"200", nullptr);
    Style style = workbook.CreateStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    font.SetColor(Color::White());
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatData.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Att förankra samma regel på rad‑fältetiketten E4 (rad 3, kolumn 4) med `Field`‑omfånget löser till F4:F6 istället – samma datakolumn utan totalsummaraden – eftersom omfånget nu beskriver `Fruit`‑fältet snarare än hela värdeområdet. `Selection`‑omfånget som förankras på F4 löser bara till F4.

## **Definiera området manuellt**
Det andra sättet hoppar över omfångsväljaren och namnger området explicit på `PivotConditionalFormat`.

### **Ett kalkylbladsrektangel med AddCellArea**
`AddCellArea(CellArea)` registrerar den angivna rektangeln som mål för regeln. Koordinaterna är nollbaserade kalkylbladskoordinater, och området är exakt den levererade rektangeln – ingen utökning till datakolumnen och ingen totalsummalogik. Använd den när de intressanta cellerna är en känd fast rektangel i den aktuella pivottabellens layout.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    U16String fruits[] = {
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Cherry"),
        U16String(u"Cherry")
    };
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    pivotTable.CalculateData();
    int32_t index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    CellArea area;
    area.StartRow = 3;
    area.EndRow = 5;
    area.StartColumn = 5;
    area.EndColumn = 5;
    format.AddCellArea(area);
    int32_t conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue,
        OperatorType::Between,
        u"150",
        u"300");
    Style style = workbook.CreateStyle();
    style.GetFont().SetIsItalic(true);
    style.SetForegroundColor(Color::LightYellow());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Ett semantiskt pivot‑område med PivotAreas**
`GetPivotAreas()` tillhandahåller samma semantiska områdesmodell som syskonsidan använder för statiska stilar. Skapa ett `PivotArea`, välj ett fält eller område med `Select` eller `SelectField`, och lägg till det med `GetPivotAreas().AddPivotArea(PivotArea)`. Ett semantiskt område förblir knutet till sitt fält, så den villkorsstyrda formateringen följer fältet när pivottabellen uppdateras och layouten förändras. `GetPivotAreas().Add(PivotArea)`‑överlagringen kompilerar fortfarande men är markerad som föråldrad – föredra `AddPivotArea`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    PivotArea area(pivotTable);
    area.SelectField(PivotFieldType::Data, u"Amount");
    format.GetPivotAreas().AddPivotArea(area);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::LessThan, u"150", nullptr);
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Gray());
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Var reglerna lagras och hur de överlever en omladdning**
Varje anrop av `pivotTable.GetConditionalFormats().Add()` lägger till ett `PivotConditionalFormat` i pivottabellen. Villkoren, deras formler och deras stilar sparas med arbetsboken – att öppna filen igen i exemplet nedan visar samma regel med sin typ, operator och formel intakt, och `GetCellAreas()` rapporterar samma områden. Poster som aldrig fick ett villkor tas bort när arbetsboken sparas, på samma sätt som Excel tar bort en villkorsstyrd formatering som saknar regel.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
static const char* ToString(FormatConditionType type)
{
    switch (type)
    {
    case FormatConditionType::CellValue:
        return "CellValue";
    default:
        return "Unknown";
    }
}
static const char* ToString(OperatorType op)
{
    switch (op)
    {
    case OperatorType::GreaterThan:
        return "GreaterThan";
    default:
        return "Unknown";
    }
}
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"PivotConditionalFormatData.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    auto conditionalFormats = pivotTable.GetConditionalFormats();
    int formatCount = conditionalFormats.GetCount();
    std::cout << "Conditional formats: " << formatCount << std::endl;
    for (int i = 0; i < formatCount; ++i)
    {
        PivotConditionalFormat format = conditionalFormats.Get(i);
        auto formatConditions = format.GetFormatConditions();
        int conditionCount = formatConditions.GetCount();
        for (int j = 0; j < conditionCount; ++j)
        {
            FormatCondition condition = formatConditions.Get(j);
            std::cout << "Format " << i << ": "
                      << ToString(condition.GetType()) << " "
                      << ToString(condition.GetOperator())
                      << " formula1=" << condition.GetFormula1().ToUtf8()
                      << std::endl;
        }
        Vector<CellArea> areas = format.GetCellAreas();
        for (int k = 0; k < areas.GetLength(); ++k)
        {
            CellArea area = areas[k];
            std::cout << "    rows " << area.StartRow + 1 << "-" << area.EndRow + 1
                      << ", columns " << area.StartColumn + 1 << "-" << area.EndColumn + 1
                      << std::endl;
        }
    }
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/cpp/apply-style-to-pivot-table/)
- [Formatera del av en pivottabell](/cells/sv/cpp/format-part-of-pivot-table/)
- [Top 10 Visa eller filtrera i pivottabell](/cells/sv/cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="cpp" >}}