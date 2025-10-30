---
title: Hur man hanterar PivotChart med PivotOptions i C++
linktitle: Pivotalternativ
type: docs
weight: 10
url: /sv/cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Hur man hanterar PivotChart med PivotOptions med C++.
keywords: PivotChart
---

## Vad är PivotChart

En PivotChart i Excel är en grafisk representation av data skapad från en PivotTable. Den låter användare visualisera och analysera data dynamiskt genom att sammanfatta och visa information i diagramform. PivotCharts är interaktiva och kan lätt modifieras för att visa olika perspektiv av data, vilket gör det till ett kraftfullt verktyg för dataanalys och presentation i Excel.

## Hur man hanterar PivotChart med PivotOptions

Genom att använda Aspose.Cells kan du använda [**PivotOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/pivotoptions/) för att hantera PivotChart.

Exempelfil och kod:  
[Exempelfil](Sample.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path for the sample Excel file
    U16String path = u"..\\Data\\01_SourceDirectory\\";

    // Create a Workbook object from the sample file
    Workbook book(path + u"Sample.xlsx");

    // Get the first chart from the first worksheet
    Chart chart = book.GetWorksheets().Get(0).GetCharts().Get(0);

    // Get the PivotOptions from the chart
    PivotOptions opt = chart.GetPivotOptions();

    // Hide ZoneFilter in PivotChart
    opt.SetDropZoneFilter(false); // HideZoneFilter

    // You can set more properties, try them!
    // opt.SetDropZoneCategories(false);  // HideZoneCategories
    // opt.SetDropZoneData(false);        // HideZoneData
    // opt.SetDropZoneSeries(false);      // HideZoneSeries
    // opt.SetDropZonesVisible(false);    // Hide All

    // Save the modified file to see the effect
    book.Save(path + u"HideZoneFilter.xlsx");

    std::cout << "Pivot chart updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Med den tidigare nämnda exempelkoden kan du kontrollera resultatfilen med följande effekt, som visas i figuren:

**![Output](Output.png)**
{{< app/cells/assistant language="cpp" >}}
