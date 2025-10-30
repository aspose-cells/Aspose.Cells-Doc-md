---
title: Ändra slicerns egenskaper med C++
linktitle: Ändra sliceregenskaper
type: docs
weight: 70
url: /sv/cpp/change-slicer-properties/
description: Ändra egenskaperna för en slicer i Excel filer med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

Det kan finnas situationer där du vill ändra egenskaperna för slicern, såsom placering eller radhöjd. Aspose.Cells ger dig möjlighet att uppdatera dessa egenskaper.

## **Ändra Slicer-egenskaper**

Var god se följande exempelkod. Den laddar in den [exempel-Excel-filen](sampleCreateSlicerToExcelTable.xlsx) som innehåller en tabell. Den skapar sedan slicern baserat på den första kolumnen och ändrar dess egenskaper som radhöjd, bredd, är utskrivbar, titel, osv. Den sparar arbetsboken som [utdataChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx).

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing a table.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook workbook(sourceDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet.
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int32_t idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    Slicer slicer = worksheet.GetSlicers().Get(idx);
    slicer.SetPlacement(PlacementType::FreeFloating);
    slicer.SetRowHeightPixel(50);
    slicer.SetWidthPixel(500);
    slicer.SetTitle(u"Aspose");
    slicer.SetAlternativeText(u"Alternate Text");
    slicer.SetIsPrintable(false);
    slicer.SetIsLocked(false);

    // Refresh the slicer.
    slicer.Refresh();

    // Save the workbook in output XLSX format.
    workbook.Save(outputDir + u"outputChangeSlicerProperties.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
