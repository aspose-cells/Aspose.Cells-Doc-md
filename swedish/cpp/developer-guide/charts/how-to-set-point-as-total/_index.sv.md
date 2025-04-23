---
title: Hur man sätter punkt som total med C++
linktitle: Hur man ställer in punkt som total
description: I vissa Excel diagram, till exempel vattenfalla diagram, kan du behöva sätta en punkt som total. Den här artikeln beskriver hur man använder Aspose.Cells med C++ för att göra det.
keywords: Vattenfallsdiagram, punkt, ställ in som total.
type: docs
weight: 72
url: /sv/cpp/how-to-set-point-as-total/
---

## Vad är "Ställ in punkt som total" i Excel-diagram

I vissa Excel-diagram, till exempel vattenfall-diagram, är vissa datapunkter summan av de föregående punkterna, och du kan behöva "ställer in punkten som total". Vi visar exempel på kod och illustration nedan.

## Ett vattenfallsdiagram behöver "Ställa in punkt som total" 

![todo:image_alt_text](set-as-total1.png)

Denna bild visar ett vattenfall-diagram i Excel. Vi kan se att det finns fyra datapunkter som börjar med "Total", och de används för att räkna alla föregående datapunkter.
I denna bild är inställningarna inte helt rätt, när vi väljer en punkt "Total 2024" och kan se att alternativet "Ställ som total" inte är markerat i Excel.
Bifogat nedan finns [exempelfilen Excel](SampleSheet.xlsx) som behöver ändras, och vi kommer att använda Aspose.Cells för att ställa in den korrekt.

## Använd Aspose.Cells för "Ställ in punkten som total" 

Vi använder följande kod för att få filen att ställas in korrekt:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize file path
    U16String filePath(u"");

    // Load the workbook
    Workbook wb(filePath + u"SampleSheet.xlsx");

    // Get the first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Get the chart by name
    Chart chart = worksheet.GetCharts().Get(u"Graphiq5");

    // Set some points as total column
    // In this example, we set points 0, 4, 8, 12 as total
    Vector<int32_t> subtotals = {0, 4, 8, 12};
    chart.GetNSeries().Get(0).GetLayoutProperties().SetSubtotals(subtotals);

    // Save the workbook
    wb.Save(filePath + u"output.xlsx");

    std::cout << "Chart subtotals set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Du kan få följande rätta [utdatafil](output.xlsx)

Som visas i figuren nedan är de fyra "Total"-datapunkterna korrekt inställda, och du kan se skillnaden från föregående diagram.

![todo:image_alt_text](set-as-total2.png)
