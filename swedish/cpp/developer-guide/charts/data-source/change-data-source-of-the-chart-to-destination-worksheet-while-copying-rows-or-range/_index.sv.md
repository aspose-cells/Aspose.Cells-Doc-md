---  
title: Ändra datakälla för diagrammet till destinationsbladet när du kopierar rader eller område med C++  
description: Lär dig hur du ändrar datakällan för ett diagram till ett destinationsblad när du kopierar rader eller ett område i Aspose.Cells for C++. Vår guide visar hur du uppdaterar diagrammets databasutdrag och länkar den till destinationsbladet, så att de kopierade raderna eller området återspeglas korrekt i diagrammet.  
keywords: Aspose.Cells for C++, diagram, datakälla, destinationsblad, rader, område, kopiera, uppdatera, dataintervall, koppling.  
type: docs  
weight: 440  
url: /sv/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Möjliga användningsscenario**

När du kopierar rader eller område som innehåller diagram till ett nytt blad förändras inte diagrammets datakälla. Till exempel, om datakällan för diagrammet är =Sheet1!$A$1:$B$4, kommer den att förbli densamma även efter att du kopierar rader eller område till ett nytt blad, dvs. =Sheet1!$A$1:$B$4. Den refererar fortfarande till det gamla bladet dvs. Sheet1. Detta är även standardbeteendet i Microsoft Excel. Men om du vill att den ska referera till det nya destinationsbladet, använd då egenskapen [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) och ställ in den till **true** när du anropar metoden [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/). Om ditt destinationsblad är DestSheet, kommer därför datakällan för ditt diagram att ändras från =Sheet1!$A$1:$B$4 till =DestSheet!$A$1:$B$4.

## **Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område**

Följande exempel kod förklarar användningen av [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/)-egendomen vid kopiering av rader eller område som innehåller diagram till ett nytt blad. Koden använder filen [exempel Excel-fil](5113699.xlsx) och genererar [output Excel-fil](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the first sheet which contains chart
    Worksheet source = wb.GetWorksheets().Get(0);

    // Add another sheet named DestSheet
    Worksheet destination = wb.GetWorksheets().Add(u"DestSheet");

    // Set CopyOptions.ReferToDestinationSheet to true
    CopyOptions options;
    options.SetReferToDestinationSheet(true);

    // Copy all the rows of source worksheet to destination worksheet which includes chart as well
    // The chart data source will now refer to DestSheet
    destination.GetCells().CopyRows(source.GetCells(), 0, 0, source.GetCells().GetMaxDisplayRange().GetRowCount(), options);

    // Save workbook in xlsx format
    wb.Save(srcDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
