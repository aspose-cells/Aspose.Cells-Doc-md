---
title: Tillämpa stilar på pivottabeller
linktitle: Tillämpa stilar på pivottabeller
description: Lär dig hur du tillämpar inbyggda och anpassade stilar på pivottabeller i Aspose.Cells for C++, inklusive äldre XLS-autoformat, moderna namngivna stilar från Excel 2007+, anpassade pivottabellstilar och genvägen FormatAll.
keywords: Aspose.Cells C++ pivottabell stil, PivotTableStyleType, AutoFormatType, FormatAll, anpassad stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /sv/cpp/apply-style-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder tillämpning av både äldre pivot-autoformat (avsedda för `.xls`-filer) och moderna namngivna eller anpassade pivottabellstilar (avsedda för `.xlsx`-, `.xlsm`- och `.xlsb`-filer). Vilket API du bör anropa beror på det filformat som arbetsboken sparas till, inte det format den laddades från.

{{% /alert %}}

## **Introduktion**

Aspose.Cells exponerar två parallella stil-API:er för pivottabeller. Valet mellan dem styrs av det filformat du sparar arbetsboken till, inte av det format du läser den från. En arbetsbok som laddats från en `.xls`-fil kan sparas om som `.xlsx`, och i så fall gäller det moderna stil-API:t snarare än det äldre.

För äldre `.xls`-utdata använder du egenskapen `PivotTable.AutoFormatType` tillsammans med enumerationen `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Detta API motsvarar den autoformatväljare som klassisk Excel erbjöd för pivottabeller.

För moderna `.xlsx`-, `.xlsm`- och `.xlsb`-utdata finns två varianter av stil-API:

- `PivotTable.PivotTableStyleType` väljer en av de inbyggda namngivna stilarna (ljust och mörkt tema, inklusive de stilar som lades till i Excel 2017). Dessa förinställningar är skrivskyddade.
- `PivotTable.PivotTableStyleName` väljer en anpassad stil som du definierar själv via `Worksheets.TableStyles.AddPivotTableStyle(...)`. Anpassade stilar krävs när du vill ändra färger, kanter eller typsnitt utöver vad förinställningarna erbjuder.

Dessutom är `PivotTable.FormatAll(Style)` en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivoten, och åsidosätter det som ställts in via någon av ovanstående stilnamn-API:er. Detta är användbart när ett enhetligt utseende krävs oavsett underliggande tema.

## **Tillämpa ett äldre XLS-förinställt autoformat**

`PivotTable.AutoFormatType` accepterar ett värde från enumerationen `Aspose.Cells.Pivot.PivotTableAutoFormatType`. De tillgängliga värdena är `Report1` till `Report10`, `Classic` och `Table1` till `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` respekteras endast när arbetsboken sparas som `.xls`. När samma arbetsbok sparas som `.xlsx`, `.xlsm` eller `.xlsb` ignorerar Excel denna egenskap och återgår till inställningarna `PivotTableStyleType` och `PivotTableStyleName`.

{{% /alert %}}

Följande exempel laddar en ny arbetsbok, fyller i exempeldata för Fruit/Year/Amount, lägger till en pivottabell, tillämpar `PivotTableAutoFormatType.Report5` och sparar resultatet som `.xls`.

{{% alert color="primary" %}}

**Varför inga kolumnfält?** Autoformaten i Report-serien (`Report1` till `Report10`, `Table1` till `Table10`) designades i klassiska Excel för **endimensionella pivottabeller** med endast radfält och värden — de har ingen inbyggd formatering för kolumnfält-rubriker. Om din pivottabell behöver kolumnfält, använd de moderna `PivotTableStyleType`-förinställningarna från Scenario 2 nedan istället, som är designade för den tvådimensionella layout som moderna Excel använder.

{{% /alert %}}

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Skapa en ny arbetsbok
    Workbook workbook;

    // Hämta det första kalkylbladet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Fyll källdatan med rubrikrad (Fruit, Year, Amount)
    // och 9 datarader som täcker grape, blueberry, kiwi, cherry under 2020 och 2021
    sheet.GetCells().Get(0, 0).PutValue(u"Fruit");
    sheet.GetCells().Get(0, 1).PutValue(u"Year");
    sheet.GetCells().Get(0, 2).PutValue(u"Amount");

    sheet.GetCells().Get(1, 0).PutValue(u"grape");
    sheet.GetCells().Get(1, 1).PutValue(2020);
    sheet.GetCells().Get(1, 2).PutValue(50);

    sheet.GetCells().Get(2, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(2, 1).PutValue(2020);
    sheet.GetCells().Get(2, 2).PutValue(30);

    sheet.GetCells().Get(3, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(3, 1).PutValue(2020);
    sheet.GetCells().Get(3, 2).PutValue(25);

    sheet.GetCells().Get(4, 0).PutValue(u"cherry");
    sheet.GetCells().Get(4, 1).PutValue(2020);
    sheet.GetCells().Get(4, 2).PutValue(40);

    sheet.GetCells().Get(5, 0).PutValue(u"grape");
    sheet.GetCells().Get(5, 1).PutValue(2021);
    sheet.GetCells().Get(5, 2).PutValue(60);

    sheet.GetCells().Get(6, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(6, 1).PutValue(2021);
    sheet.GetCells().Get(6, 2).PutValue(35);

    sheet.GetCells().Get(7, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(7, 1).PutValue(2021);
    sheet.GetCells().Get(7, 2).PutValue(28);

    sheet.GetCells().Get(8, 0).PutValue(u"cherry");
    sheet.GetCells().Get(8, 1).PutValue(2021);
    sheet.GetCells().Get(8, 2).PutValue(45);

    sheet.GetCells().Get(9, 0).PutValue(u"grape");
    sheet.GetCells().Get(9, 1).PutValue(2020);
    sheet.GetCells().Get(9, 2).PutValue(45);

    // Lägg till en pivottabell vid målcell E3, namngiven "Pivot1", med användning av källintervallet A1:C10
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    // Tilldela fält: Fruit -> Rader, Year -> Kolumner, Amount -> Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Tillämpa det äldre XLS-förinställda autoformatet "Report5"
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // Spara arbetsboken i äldre .xls-format
    workbook.Save(u"output.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Tillämpa en modern namngiven förinställd pivottabellstil**

`PivotTable.PivotTableStyleType` accepterar ett värde från enumerationen `Aspose.Cells.PivotTableStyleType`. Enumerationen täcker ljusa teman `PivotTableStyleLight1` till `PivotTableStyleLight28` och mörka teman `PivotTableStyleDark1` till `PivotTableStyleDark28`. Stilarna som lades till i Excel 2017 (den andra vågen av ljusa och mörka teman) kan nås via samma enumeration.

Detta är det rekommenderade API:t för alla moderna filformat. Till skillnad från det äldre autoformatet renderas stilen som väljs här troget av Excel och överlever rundresor genom andra Office-verktyg.

Följande exempel använder samma Fruit/Year/Amount-data, skapar en identisk pivottabell, tillämpar `PivotTableStyleDark1` och sparar arbetsboken som `.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(150);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(200);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(180);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(120);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(170);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(210);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(190);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(130);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Definiera och tillämpa en anpassad pivottabellstil**

De inbyggda förinställningarna kan inte ändras. När du behöver åsidosätta färger, kanter eller typsnitt måste du definiera en anpassad pivotstil. Arbetsflödet har tre steg:

1. Lägg till en anpassad stil i arbetsbokens `TableStyles`-samling via `Worksheets.TableStyles.AddPivotTableStyle(string name)`. Detta returnerar indexet för den nyskapade stilen.
2. Konfigurera stilen genom att lägga till element (såsom `WholeTable` eller `GrandTotalRow`) via `TableStyle.TableStyleElements.Add(TableStyleElementType)`, och tilldela sedan en `Style` till varje element via `TableStyleElement.SetElementStyle(Style)`.
3. Tillämpa den anpassade stilen på pivoten genom att sätta `PivotTable.PivotTableStyleName` till stilens namn. Använd inte `PivotTableStyleType` här, eftersom den egenskapen väljer inbyggda förinställningar.

{{% alert color="primary" %}}

`PivotTableStyleName` och `PivotTableStyleType` är inte utbytbara. Använd `PivotTableStyleType` för inbyggda förinställningar, och `PivotTableStyleName` för anpassade stilar som du har definierat via `AddPivotTableStyle`. Att sätta båda är ofarligt, men endast den som matchar den avsedda källan renderas.

{{% /alert %}}

De tillgängliga `TableStyleElementType`-värdena inkluderar `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` och `PageFieldValues`.

Följande exempel definierar en anpassad pivotstil med en tunn svart kant på `WholeTable` och ett fet rött typsnitt på `GrandTotalRow`, och tillämpar den sedan via `PivotTableStyleName` och sparar som `.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    // Fyll i källdata: rubrikrad + 9 datarader (A1:C10)
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    // Lägg till pivottabell med källa från A1:C10, förankrad vid E3, med namnet "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Steg 1: registrera en ny anpassad pivottabellstil och fånga dess index
    int styleIndex = workbook.GetWorksheets().GetTableStyles().AddPivotTableStyle(u"CustomPivotStyle");
    TableStyle tableStyle = workbook.GetWorksheets().GetTableStyles().Get(styleIndex);

    // Steg 2: lägg till ett WholeTable-element och tillämpa tunna svarta kanter på alla fyra sidor
    int wholeTableElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::WholeTable);
    TableStyleElement wholeTableElement = tableStyle.GetTableStyleElements().Get(wholeTableElementIndex);
    Style wholeTableStyle = workbook.CreateStyle();
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    wholeTableElement.SetElementStyle(wholeTableStyle);

    // Steg 3: lägg till ett GrandTotalRow-element och tillämpa fet röd font
    int grandTotalElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::GrandTotalRow);
    TableStyleElement grandTotalElement = tableStyle.GetTableStyleElements().Get(grandTotalElementIndex);
    Style grandTotalStyle = workbook.CreateStyle();
    grandTotalStyle.GetFont().SetIsBold(true);
    grandTotalStyle.GetFont().SetColor(Color::Red());
    grandTotalElement.SetElementStyle(grandTotalStyle);

    // Steg 4: tillämpa den anpassade stilen med namn (INTE via PivotTableStyleType, vilket är för inbyggda förinställningar)
    pivotTable.SetPivotTableStyleName(u"CustomPivotStyle");

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Tillämpa en stil på varje pivotcell med FormatAll**

`PivotTable.FormatAll(Style)` är en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen, inklusive dataområdet, rad- och kolumnrubriker samt summor. Det som tidigare ställts in via `PivotTableStyleType` eller `PivotTableStyleName` åsidosätts.

{{% alert color="primary" %}}

`FormatAll` åsidosätter både `PivotTableStyleType` och `PivotTableStyleName`. Använd det endast när ett enhetligt, temaoberoende utseende krävs över hela pivoten.

{{% /alert %}}

Följande exempel skapar en `Style` med gul solid fyllning, ett fett mörkblått typsnitt och tunna svarta kanter på alla sidor, och tillämpar den sedan med `FormatAll` och sparar som `.xlsx`.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Huvudrad
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // Datarader
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(5000);

    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(3000);

    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(4000);

    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(2000);

    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(6000);

    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(3500);

    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(4500);

    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(2500);

    worksheet.GetCells().Get(u"A10").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B10").PutValue(2021);
    worksheet.GetCells().Get(u"C10").PutValue(5500);

    // Lägg till pivottabell: källområde A1:C10, målcell E3, namn "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Tilldela pivotfält
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Bygg en stil som tvingas på varje cell i pivottabellen
    Style style = wb.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);
    style.GetFont().SetIsBold(true);
    style.GetFont().SetColor(Color::DarkBlue());
    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    // Tillämpa FormatAll
    pivotTable.FormatAll(style);

    // Spara arbetsboken
    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Vilket stil-API bör jag använda?**

Valet av stil-API beror på det filformat du sparar till. Använd tabellen nedan som en snabbreferens.

| Målfilformat | API att använda | Anteckningar |
|---|---|---|
| `.xls` (äldre) | `PivotTable.AutoFormatType` | Värden från `Aspose.Cells.Pivot.PivotTableAutoFormatType` (t.ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignoreras vid sparning som moderna format. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, inbyggd stil) | `PivotTable.PivotTableStyleType` | Värden från `Aspose.Cells.PivotTableStyleType` (ljusa/mörka teman, inklusive tillägg från Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, anpassad stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Använd när de inbyggda förinställningarna inte räcker. Konfigurera via `TableStyleElement.SetElementStyle(...)`. |
| Alla format (enhetlig åsidosättning) | `PivotTable.FormatAll(Style)` | Genväg som åsidosätter alla andra stilinställningar över hela pivoten. |

Vid tvivel, spara som `.xlsx` och använd `PivotTableStyleType` för inbyggda teman, eller `PivotTableStyleName` för anpassade teman.

{{< app/cells/assistant language="cpp" >}}