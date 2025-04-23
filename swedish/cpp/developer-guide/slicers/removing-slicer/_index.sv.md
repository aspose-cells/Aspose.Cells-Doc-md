---
title: Ta bort slicer med C++
linktitle: Ta bort slicer
type: docs
weight: 30
url: /sv/cpp/removing-slicer/
description: Lär dig hur du tar bort slicers i Excel filer programmässigt med hjälp av Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Om du vill ta bort en slicer i Microsoft Excel, välj den och tryck på *Delete*-knappen. På liknande sätt, om du vill ta bort den med Aspose.Cells API-programmering, använd [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/remove/)-metoden. Det tar bort slicern från arket.

## **Ta bort slicer**

Följande exempelkod laddar den [provmappen](67338478.xlsx) som innehåller en befintlig snitt. Den kommer åt snittet och tar bort det. Slutligen sparar den arbetsboken som [utmatningsmapp](67338477.xlsx). Följande skärmbild visar snittet som kommer att tas bort efter körningen av exempelkoden.

![todo:image_alt_text](removing-slicer_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath(u"sampleRemovingSlicer.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet.
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access the first slicer inside the slicer collection.
    SlicerCollection slicers = ws.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Remove slicer.
    slicers.Remove(slicer);

    // Save the workbook in output XLSX format.
    U16String outputFilePath(u"outputRemovingSlicer.xlsx");
    wb.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Slicer removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
