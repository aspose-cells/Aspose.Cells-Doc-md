---
title: Hur man ställer in serie som osynlig med C++
linktitle: Hur man sätter serien osynlig
description: I Excel diagram kan du behöva göra serier osynliga. Denna artikel beskriver hur man använder Aspose.Cells med C++ för att göra detta.
keywords: Excel diagram, Serie, Osynlig, ÄrFiltrerad.
type: docs
weight: 74
url: /sv/cpp/how-to-set-series-invisible/
---

## Hur man ställer in serie som osynlig i Excel-diagram

I Excel-diagram kan du högerklicka på ett diagram, klicka på "Välj data" och i pop-up-fönstret kan du ställa in om en serie är synlig genom att markera eller avmarkera den. Du kan ladda ner följande [exempelfil](SeriesFiltered.xlsx) och använda den i Excel enligt figuren för att uppnå denna funktion. Nästa steg är att visa dig hur du uppnår detta med Aspose.Cells-biblioteket.

![todo:image_alt_text](series-invisible.png)

## Hur man ställer in serie som osynlig med Aspose.Cells 

Vi använder följande kod för att göra serie osynlig med Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // File path for the input and output Excel files
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file
    Workbook workbook(filePath + u"SeriesFiltered.xlsx");

    // Access the charts collection of the first worksheet
    ChartCollection charts = workbook.GetWorksheets().Get(0).GetCharts();

    // Access a specific chart by name
    Chart chart = charts.Get(u"Chart 1");

    // Access filtered and non-filtered series collections
    SeriesCollection nSeriesFiltered = chart.GetFilteredNSeries();
    SeriesCollection nSeries = chart.GetNSeries();

    // Set the visibility of the first two series to be filtered
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Save the modified Excel file
    workbook.Save(filePath + u"output.xlsx");

    std::cout << "Series filtered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Du kan hämta följande [Inmatningsfil](SeriesFiltered.xlsx) och [Utdatafil](output.xlsx).

Som visas i figuren nedan har de två första serierna, som ursprungligen var synliga, blivit osynliga i utdatafilen.  
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="cpp" >}}
