---
title: Ändra sidfältslayout i pivottabell
linktitle: Ändra sidfältslayout i pivottabell
description: Lär dig hur du styr layouten för sidfältsområdet i en pivottabell med Aspose.Cells for C++, inklusive att ställa in visningsordning, radbrytningsantal och fältordning för sidfälten högst upp i pivottabellen.
keywords: Aspose.Cells, C++-bibliotek, kalkylblad, pivottabell, sidfält, sidfältsordning, radbrytningsantal för sidfält, flytta sidfält
type: docs
weight: 191
url: /sv/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Den här artikeln är en fortsättning på ämnet **Lägg till sidfält i pivottabell**. Den visar hur man styr layouten för sidfältsområdet — remsan av filterkontroller högst upp i en pivottabell — inklusive visningsordning, radbrytningsantal och omordning av fält.
{{% /alert %}}
## **Introduktion**
En pivottabell i Microsoft Excel har ett dedikerat **sidfältsområde** som sitter ovanför tabellens rad-, kolumn- och datakropp. Detta område renderas som en remsa av rullgardinsfilterkontroller (en per sidfält) och det är detta som slutanvändare klickar på för att skära pivoten efter kriterier som år eller region. Aspose.Cells for C++ modellerar detta område via samlingen `PivotTable.PageFields` och exponerar tre egenskaper som styr hur remsan visas visuellt:
- `PivotTable.PageFieldOrder` (ett `Aspose.Cells.PrintOrderType`-värde) avgör om ytterligare sidfält placeras *bredvid* de befintliga eller *under* dem.
- `PivotTable.PageFieldWrapCount` anger hur många sidfält som placeras per rad eller kolumn innan de bryts.
- `PivotTable.PageFields.Move(currIndex, destIndex)` omordnar sidfälten utan att ändra ordningsläget.
Den här artikeln går igenom tre kodexempel som demonstrerar var och en av dessa operationer på en delad datamängd, så att du kan jämföra de resulterande layouterna sida vid sida.
## **Källdata**
Alla tre exempel nedan läser in dessa åtta rader försäljningsdata i ett kalkylblad med namnet `PivotData`. Data innehåller två sidfältskandidater (`Year`, `Region`), en radfältskandidat (`Fruit`) och ett mått (`Amount`), vilket gör att sidfältsremsan blir meningsfull att inspektera.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Alla åtta raderna fylls i i varje kodexempel, i identisk ordning, så källdata skiljer sig aldrig åt mellan scenarierna — det är bara egenskaperna för sidfältslayouten som skiljer sig åt.
## **Exempel 1: Över sedan ned**
I det första scenariot konfigurerar vi de två sidfälten (`Year`, `Region`) så att de visas **sida vid sida i en enda rad** högst upp i pivottabellen. Vi tilldelar `Fruit` till radaxeln, placerar `Year` först och `Region` sedan på sidaxeln (ordningen på `AddFieldToArea`-anropen bestämmer startindex), lägger till `Amount` (`Sum`) som datafält, och ställer sedan in `PageFieldOrder` till `PrintOrderType.OverThenDown` med `PageFieldWrapCount = 2`. Med `OverThenDown` och ett radbrytningsantal på 2, läggs de två sidfälten ut horisontellt sida vid sida i en enda rad högst upp i pivottabellen, så att remsan upptar en rad med bredden två.
```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "output";
    if (!std::filesystem::exists(dataDir)) {
        std::filesystem::create_directories(dataDir);
    }

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();

    Worksheet pivotDataSheet = worksheets.Add(u"PivotData");
    Cells pivotDataCells = pivotDataSheet.GetCells();

    // Rubriker (rad 0)
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");

    // Rad 1: Apple, 2022, North, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);

    // Rad 2: Apple, 2023, North, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);

    // Rad 3: Banana, 2022, South, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);

    // Rad 4: Banana, 2023, South, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);

    // Rad 5: Cherry, 2022, East, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);

    // Rad 6: Cherry, 2023, East, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);

    // Rad 7: Grape, 2022, West, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);

    // Rad 8: Grape, 2023, West, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);

    // Lägg till PivotTableReport-ark
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();

    // Skapa pivottabell med källa från PivotData!A1:D9 placerad vid A1 på PivotTableReport
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Lägg till fält
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Fruit
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Year
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Region
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Amount
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    // Konfigurera layout för sidfältsområde: placera sidfält först horisontellt, radbrytning efter varannan
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    // Uppdatera och beräkna
    pivotTable.CalculateData();

    // Spara
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Exempel 2: Ned sedan över**
I det här exemplet placerar vi `Fruit` på radaxeln, `Year` och `Region` på sidaxeln (med `Year` först), och `Amount` (`Sum`) som datafält — precis som i Exempel 1. Vi ställer sedan in `PageFieldOrder` till `PrintOrderType.DownThenOver` och `PageFieldWrapCount` till `2`. Med `DownThenOver` och ett radbrytningsantal på 2, staplas de två sidfälten vertikalt — `Year` överst, `Region` direkt nedanför — och bildar en enda kolumn högst upp i pivottabellen. Remsan upptar alltså två rader med bredden ett, till skillnad från Exempel 1.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet pivotData = workbook.GetWorksheets().Get(0);
    pivotData.SetName(u"PivotData");
    Worksheet pivotReport = workbook.GetWorksheets().Add(u"PivotTableReport");

    const char* headers[] = { "Fruit", "Year", "Region", "Amount" };
    for (int c = 0; c < 4; c++)
    {
        pivotData.GetCells().Get(0, c).PutValue(U16String(headers[c]));
    }

    struct DataRow {
        U16String fruit;
        int year;
        U16String region;
        int amount;
    };

    DataRow data[] = {
        {U16String("Apple"),  2022, U16String("North"), 150},
        {U16String("Apple"),  2023, U16String("North"), 180},
        {U16String("Banana"), 2022, U16String("South"), 120},
        {U16String("Banana"), 2023, U16String("South"), 140},
        {U16String("Cherry"), 2022, U16String("East"),  200},
        {U16String("Cherry"), 2023, U16String("East"),  220},
        {U16String("Grape"),  2022, U16String("West"),  90},
        {U16String("Grape"),  2023, U16String("West"),  110}
    };

    for (int r = 0; r < 8; r++)
    {
        pivotData.GetCells().Get(r + 1, 0).PutValue(data[r].fruit);
        pivotData.GetCells().Get(r + 1, 1).PutValue(data[r].year);
        pivotData.GetCells().Get(r + 1, 2).PutValue(data[r].region);
        pivotData.GetCells().Get(r + 1, 3).PutValue(data[r].amount);
    }

    int idx = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", u"A1", u"PivotTable");
    PivotTable pivotTable = pivotReport.GetPivotTables().Get(idx);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.CalculateData();

    workbook.Save(u"pageFieldLayout_downThenOver.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Exempel 3: Flytta ett sidfält**
I det tredje scenariot behåller vi denna datamängd och fälttilldelning, ställer in en neutral layout (`OverThenDown` med radbrytningsantal `2`), och demonstrerar sedan `PageFields.Move`-operationen. Anropet `Move(0, 1)` flyttar sidfältet på index 0 (`Year`) till position 1, och sidfältet som var på position 1 (`Region`) flyttas till position 0. Efter detta anrop är `Region` det första sidfältet och `Year` är det andra. Radbrytningen och ordningsläget är oförändrade, så remsan renderas fortfarande horisontellt sida vid sida — det är bara ordningen på de två rullgardinsmenyerna som har bytts om.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet dataSheet = wb.GetWorksheets().Get(0);
    dataSheet.SetName(u"PivotData");

    Cells dataCells = dataSheet.GetCells();

    dataCells.Get(u"A1").PutValue(u"Fruit");
    dataCells.Get(u"B1").PutValue(u"Year");
    dataCells.Get(u"C1").PutValue(u"Region");
    dataCells.Get(u"D1").PutValue(u"Amount");

    dataCells.Get(u"A2").PutValue(u"Apple");
    dataCells.Get(u"B2").PutValue(2022);
    dataCells.Get(u"C2").PutValue(u"North");
    dataCells.Get(u"D2").PutValue(150);

    dataCells.Get(u"A3").PutValue(u"Apple");
    dataCells.Get(u"B3").PutValue(2023);
    dataCells.Get(u"C3").PutValue(u"North");
    dataCells.Get(u"D3").PutValue(180);

    dataCells.Get(u"A4").PutValue(u"Banana");
    dataCells.Get(u"B4").PutValue(2022);
    dataCells.Get(u"C4").PutValue(u"South");
    dataCells.Get(u"D4").PutValue(120);

    dataCells.Get(u"A5").PutValue(u"Banana");
    dataCells.Get(u"B5").PutValue(2023);
    dataCells.Get(u"C5").PutValue(u"South");
    dataCells.Get(u"D5").PutValue(140);

    dataCells.Get(u"A6").PutValue(u"Cherry");
    dataCells.Get(u"B6").PutValue(2022);
    dataCells.Get(u"C6").PutValue(u"East");
    dataCells.Get(u"D6").PutValue(200);

    dataCells.Get(u"A7").PutValue(u"Cherry");
    dataCells.Get(u"B7").PutValue(2023);
    dataCells.Get(u"C7").PutValue(u"East");
    dataCells.Get(u"D7").PutValue(220);

    dataCells.Get(u"A8").PutValue(u"Grape");
    dataCells.Get(u"B8").PutValue(2022);
    dataCells.Get(u"C8").PutValue(u"West");
    dataCells.Get(u"D8").PutValue(90);

    dataCells.Get(u"A9").PutValue(u"Grape");
    dataCells.Get(u"B9").PutValue(2023);
    dataCells.Get(u"C9").PutValue(u"West");
    dataCells.Get(u"D9").PutValue(110);

    Worksheet pivotSheet = wb.GetWorksheets().Add(u"PivotTableReport");

    int32_t pivotIndex = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", u"A3", u"PivotTable");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.GetPageFields().Move(0, 1);

    pivotTable.CalculateData();

    wb.Save(u"pageFieldLayout_move.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Relaterade artiklar**
- [Lägg till sidfält i pivottabell](/cells/sv/cpp/add-page-field-in-pivot-table/) — föräldrasidan som introducerar hur sidfält läggs till i en pivottabell.
- [Rad- och kolumnfält i pivottabell](/cells/sv/cpp/row-and-column-fields/) — täcker allokering av fält till rad- och kolumnaxlarna, vilket kompletterar sidaxel-arbetet som visas här.
- [Hantera värdefält i pivottabell](/cells/sv/cpp/manage-value-fields/) — beskriver hur man konfigurerar data- (värde-) området, inklusive `Sum`-aggregeringen som används i denna artikel.
- [Uppdatera pivottabell](/cells/sv/cpp/refresh-pivot-table/) — förklarar `RefreshData` och `CalculateData`, vilka krävs efter omordning av sidfält.
- [Tillämpa stil på pivottabell](/cells/sv/cpp/apply-style-to-pivot-table/) — visar hur man formaterar den renderade pivottabellen efter att sidfältsremsan har lagts ut.
{{< app/cells/assistant language="" >}}