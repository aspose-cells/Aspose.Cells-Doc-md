---
title: Infoga slicer med C++
linktitle: Slicers
type: docs
weight: 170
url: /sv/cpp/create-slicer/
description: Hantera slicers i Excel filer med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

En slicer används för att filtrera data snabbt. Den kan användas för att filtrera data i både tabeller och pivottabeller. Microsoft Excel tillåter dig att skapa en slicer genom att välja en tabell eller pivottabell och klicka på *Infoga > Slicer*. Aspose.Cells tillåter också att du skapar en slicer med [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/add/)-metoden.

## **Skapa skärva till en pivot-tabell**

Se följande exempelkod. Den laddar den [prov-Excel-filen](67338470.xlsx) som innehåller pivottabellen. Den skapar sedan slicern baserad på det första baspivottfältet. Slutligen sparar den arbetsboken i [utmatnings-XLSX](67338471.xlsx) och [utmatnings-XLSB](67338472.xlsb) format. Följande skärmbild visar slicern skapad av Aspose.Cells i den utmatnings-Excel-filen.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
using namespace Aspose::Cells::Slicers;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCreateSlicerToPivotTable.xlsx";

    // Path of output Excel files
    U16String outputFilePathXlsx = outDir + u"outputCreateSlicerToPivotTable.xlsx";
    U16String outputFilePathXlsb = outDir + u"outputCreateSlicerToPivotTable.xlsb";

    // Load sample Excel file containing pivot table
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table inside the worksheet
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Add slicer relating to pivot table with first base field at cell B22
    int idx = ws.GetSlicers().Add(pt, u"B22", pt.GetBaseFields().Get(0));

    // Access the newly added slicer from slicer collection
    Slicer slicer = ws.GetSlicers().Get(idx);

    // Save the workbook in output XLSX format
    wb.Save(outputFilePathXlsx, SaveFormat::Xlsx);

    // Save the workbook in output XLSB format
    wb.Save(outputFilePathXlsb, SaveFormat::Xlsb);

    std::cout << "Slicer created and workbooks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Skapa skärva till Excel-tabell**

Vänligen se det följande provkoden. Den laddar [provmappen](sampleCreateSlicerToExcelTable.xlsx) som innehåller en tabell. Sedan skapar den en slicer baserad på den första kolumnen. Slutligen sparar den arbetsboken i [output XLSX](outputCreateSlicerToExcelTable.xlsx) format.

### **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file containing a table
    Workbook workbook(srcDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    // Save the workbook in output XLSX format
    workbook.Save(outDir + u"outputCreateSlicerToExcelTable.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer added successfully to the Excel table!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Avancerade ämnen**
- [Ändra Slicer-egenskaper](/cells/sv/cpp/change-slicer-properties/)
- [Rita Slicer vid rendering av Excel till PDF](/cells/sv/cpp/draw-slicer-while-rendering-excel-to-pdf/)
- [Formatera skärva](/cells/sv/cpp/formatting-slicer/)
- [Ta bort slicer](/cells/sv/cpp/removing-slicer/)
- [Rendering slicer](/cells/sv/cpp/rendering-slicer/)
- [Uppdatera slicer](/cells/sv/cpp/updating-slicer/)
{{< app/cells/assistant language="cpp" >}}
