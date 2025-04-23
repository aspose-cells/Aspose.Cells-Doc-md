---
title: Ta bort pivottabellanslutning med C++
linktitle: Ta bort pivotkoppling
type: docs
weight: 30
url: /sv/cpp/remove-pivot-connection/
description: Lär dig hur du tar bort pivottabellanslutning med Aspose.Cells biblioteket med C++.
keywords: Ta bort pivotkoppling utan Office 2013, Office 2016, Office 2019 och Office 365.
---

## **Möjliga användningsscenario**

Om du vill avassociera en slicer och en pivottabell i Excel, måste du högerklicka på slicern och välja "Rapportkopplingar...". I alternativlistan kan du använda kryssrutan. På liknande sätt om du vill avassociera en slicer och pivottabell med Aspose.Cells API programmatiskt, använd [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/removepivotconnection/)-metoden. Den kommer att avassosciera slicern och pivottabellen.

## **Bryt isär snitt och pivottabell**

Följande provkod laddar in [provmappen](remove-pivot-connection.xlsx) som innehåller en befintlig slicer. Den går igenom slicerna och sedan avassocierar den slicern och pivottabellen. Slutligen sparar den arbetsboken som [output Excel-fil](remove-pivot-connection-out.xlsx). 

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer
    U16String inputFilePath = u"remove-pivot-connection.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTable pivottable = ws.GetPivotTables().Get(0);

    // Access the first slicer inside the slicer collection
    Slicer slicer = ws.GetSlicers().Get(0);

    // Remove PivotTable connection
    slicer.RemovePivotConnection(pivottable);

    // Save the workbook in output XLSX format
    U16String outputFilePath = u"remove-pivot-connection-out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot connection removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
