---
title: Uppdatera och beräkna pivottabell med beräknade objekt med C++
linktitle: Uppdatera och beräkna pivottabell med beräknade poster
type: docs
weight: 40
url: /sv/cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Uppdatera och beräkna pivottabell med beräknade objekt med Aspose.Cells i C++.
---

{{% alert color="primary" %}}

Aspose.Cells stöder nu uppdatering och beräkning av pivottabell med beräknade poster. Använd vanligtvis [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) och [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) för att utföra denna funktion.

{{% /alert %}}

## **Uppdatera och beräkna pivottabell med beräknade poster**

Följande exempel laddar [käll-Excel-fil](5115238.xlsx) som innehåller en pivottabell med tre beräknade objekt, såsom "add", "div", "div2". Vi ändrar först värdet i cell D2 till 20 och uppdaterar sedan och beräknar pivottabellen med Aspose.Cells API:er och sparar arbetsboken i PDF-format. Resultatet i [utdata-PDF](5115229.pdf) visar att Aspose.Cells framgångsrikt uppdaterade och beräknade pivottabellen med beräknade objekt. Du kan verifiera detta manuellt i Microsoft Excel genom att sätta värdet 20 i cell D2 och sedan uppdatera pivottabellen via tangentkombinationen Alt+F5 eller genom att klicka på pivottabellens Uppdatera-knapp.

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

    // Load source Excel file containing a pivot table having calculated items
    U16String sampleFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(sampleFilePath);

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell D2
    sheet.GetCells().Get(u"D2").PutValue(20);

    // Refresh and calculate all the pivot tables inside this sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    for (int32_t i = 0; i < pivotTables.GetCount(); ++i)
    {
        PivotTable pt = pivotTables.Get(i);
        pt.RefreshData();
        pt.CalculateData();
    }

    // Save the workbook in output PDF
    U16String outputFilePath = srcDir + u"RefreshAndCalculateItems_out.pdf";
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
