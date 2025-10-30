---
title: Tre metoder för att filtrera diagramdata med C++
linktitle: Tre metoder för att filtrera Diagramdata
description: Lär dig hur du filtrerar diagram i Excel med Aspose.Cells for C++. Vår omfattande guide visar hur man tillämpar filter på diagram, anpassar diagramfunktioner och använder dataanalysverktyg för bättre insikter och mer informerade beslut.
keywords: Aspose.Cells for C++, Filtrera diagram i Excel, Dataanalys, Beslutsfattande, Visualisering.
type: docs
weight: 2210
url: /sv/cpp/filtering-charts-in-excel/
---


## **1. Filtrera bort serier för att rendera ett diagram**

### **Steg för att filtrera serier från ett diagram i Excel**
I Excel kan vi filtrera ut specifika serier från ett diagram, vilket gör att dessa filtrerade serier inte visas i diagrammet. Det ursprungliga diagrammet visas i **Figur 1**. Men när vi filtrerar ut **Testseriek2** och **Testseriek4**, kommer diagrammet att se ut som i **Figur 2**.

I Aspose.Cells kan vi utföra en liknande operation. För en [exempelfil](seriesFiltered.xlsx) som denna, om vi vill filtrera ut **Testseries2** och **Testseries4**, kan vi köra följande kod. Dessutom kommer vi att behålla två listor: en ([GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/)) lista för att lagra alla valda serier och en annan ([GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)) för att lagra de filtrerade serierna.

Vänligen **observera** att i koden, när vi sätter **chart->GetNSeries()->Get(0)->SetIsFiltered(true);**, tas den första serien i [GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/) bort och placeras i rätt position inom [GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/). Därefter blir den tidigare **NSeries[1]** det nya första objektet i listan, och alla följande serier flyttas framåt med ett steg. Detta innebär att om vi sedan kör **chart->GetNSeries()->Get(1)->SetIsFiltered(true);**, tar vi effektivt bort den ursprungliga tredje serien. Detta kan ibland leda till förvirring, så vi rekommenderar att följa operationen i koden, vilken tar bort serier från slutet till början.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Exempelkod**
Följande kodexempel laddar den [exempelfil i Excel](seriesFiltered.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of existing Workbook
    Workbook workbook(u"seriesFiltered.xlsx");

    // Get filtered series list
    SeriesCollection nSeriesFiltered = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetFilteredNSeries();

    // Get selected series list
    SeriesCollection nSeries = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetNSeries();

    // Should be 0
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 6
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Process from the end to the beginning
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Save the workbook
    workbook.Save(u"seriesFiltered-out.xlsx");

    // Reload the workbook
    workbook = Workbook(u"seriesFiltered-out.xlsx");

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **2. Filtrera datan och låt diagrammet ändras**

Att filtrera dina data är ett bra sätt att hantera diagramfilter med mycket data. När du filtrerar data, förändras diagrammet. En lösning vi måste ta itu med är att se till att diagrammet stannar på skärmen. När du filtrerar får du dolda rader, och ibland är diagrammet i dessa dolda rader.

![todo:image_alt_text](Figure3.png)

### **Steg för att använda Datafilter för att ändra diagrammet i Excel**

1. Klicka inom ditt datarange.
2. Klicka på fliken **Data**, och slå på filter genom att klicka på Filter. Din rubrikrad kommer att ha nedrullningspilar.
3. Skapa ett diagram genom att gå till fliken **Infoga** och välja en kolumnsdiagram.
4. Filtrera nu din data med hjälp av nedrullningspilarna i datan. Använd inte Diagramfilter.

### **Exempelkod**
Följande exempel kod visar samma funktion med Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the First sheet.
    Worksheet sheet = workbook.GetWorksheets().Get(u"Sheet1");

    // Add data into details cells.
    sheet.GetCells().Get(0, 0).PutValue(u"Fruits Name");
    sheet.GetCells().Get(0, 1).PutValue(u"Fruits Price");
    sheet.GetCells().Get(1, 0).PutValue(u"Apples");
    sheet.GetCells().Get(2, 0).PutValue(u"Bananas");
    sheet.GetCells().Get(3, 0).PutValue(u"Grapes");
    sheet.GetCells().Get(4, 0).PutValue(u"Oranges");
    sheet.GetCells().Get(1, 1).PutValue(5);
    sheet.GetCells().Get(2, 1).PutValue(2);
    sheet.GetCells().Get(3, 1).PutValue(1);
    sheet.GetCells().Get(4, 1).PutValue(4);

    // Add a chart to the worksheet
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);

    // Access the instance of the newly added chart
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B5", true);

    // Set AutoFilter range
    sheet.GetAutoFilter().SetRange(u"A1:B5");

    // Add filters for a filter column.
    sheet.GetAutoFilter().AddFilter(0, u"Bananas");
    sheet.GetAutoFilter().AddFilter(0, u"Oranges");

    // Apply the filters
    sheet.GetAutoFilter().Refresh();

    // Save the chart as an image
    chart.ToImage(u"Autofilter.png");

    // Save the workbook
    workbook.Save(u"Autofilter.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3. Filtrera datan med ett tabell och låt diagrammet ändras**

Att använda en tabell är liknande som metod 2, som använder ett intervall, men du har fördelar med tabeller över intervall. När du ändrar ditt intervall till en tabell och lägger till data, uppdateras diagrammet automatiskt. Med ett intervall måste du ändra datakällan.

### **Formatera som tabell i Excel**

Klicka inuti din data och använd **CTRL + T** eller använd fliken Hem, **Formatera som tabell**

![todo:image_alt_text](Figure4.png)

### **Exempelkod**
Följande exempelkod laddar [provfilen](TableFilters.xlsx) som visar samma funktion med Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Tables;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook
    Workbook workbook(u"TableFilters.xlsx");

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the instance of the newly added chart
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B7", true);

    // Convert the chart to image
    chart.ToImage(u"TableFilters.before.png");

    // Add a new List Object to the worksheet
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(u"A1", u"B7", true));

    // Add default style to the table
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium10);

    // Show Total
    listObject.SetShowTotals(false);

    // Add filters for a filter column
    listObject.GetAutoFilter().AddFilter(0, u"James");

    // Apply the filters
    listObject.GetAutoFilter().Refresh();

    // After adding new value the chart will change
    listObject.PutCellValue(7, 0, Object(u"Me"));
    listObject.PutCellValue(7, 1, Object(1000));

    // Check the changed images
    chart.ToImage(u"TableFilters.after.png");

    // Saving the Excel file
    workbook.Save(u"TableFilter.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
