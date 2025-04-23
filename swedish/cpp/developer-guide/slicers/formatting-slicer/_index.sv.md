---
title: Formatera slicer med C++
linktitle: Formatering av Slicer
type: docs
weight: 20
url: /sv/cpp/formatting-slicer/
description: Formatera slicers i Microsoft Excel med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

Du kan formatera slicern i Microsoft Excel genom att ställa in antalet kolumner eller genom att ställa in dess stil etc. Aspose.Cells tillåter dig också att göra detta med hjälp av [**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getnumberofcolumns/) och [**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/) egenskaper.

## **Formatera skärva**

Se följande kod; den laddar filen [sample Excel](67338473.xlsx) som innehåller en slicer. Den nås slicern och ställer in dess antal kolumner och stiltyp och sparar den som [utdata Excel](67338474.xlsx). Skärmbilden visar hur slicern ser ut efter att ha kört exemplet.

![todo:image_alt_text](formatting-slicer_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleFormattingSlicer.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = worksheet.GetSlicers().Get(0);

    // Set the number of columns of the slicer.
    slicer.SetNumberOfColumns(2);

    // Set the type of slicer style.
    slicer.SetStyleType(SlicerStyleType::SlicerStyleLight6);

    // Save the workbook in output XLSX format.
    workbook.Save(u"outputFormattingSlicer.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer formatted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
