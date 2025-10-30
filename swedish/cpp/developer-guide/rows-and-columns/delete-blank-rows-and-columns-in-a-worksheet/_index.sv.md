---
title: Ta bort tomma rader och kolumner i ett kalkblad med C++
linktitle: Radera tomma rader och kolumner i ett kalkylblad
type: docs
weight: 300
url: /sv/cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Ta bort tomma rader och kolumner i ett kalkylblad med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Det är möjligt att ta bort alla tomma rader och kolumner från ett kalkylblad. Detta är användbart när man, till exempel, genererar en PDF-fil från en Microsoft Excel-fil och vill konvertera endast rader och kolumner som innehåller data eller relaterade objekt.

Använd följande Aspose.Cells-metoder för att ta bort tomma rader och kolumner:

1. För att ta bort tomma rader, använd metoden [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankrows/). Observera, för tomma rader som kommer att tas bort, krävs det inte bara att [**Row.IsBlank**](https://reference.aspose.com/cells/cpp/aspose.cells/row/isblank/) ska vara sant, utan det får inte heller finnas någon synlig kommentar definierad för någon cell i dessa rader, och ingen pivottabell vars omfång korsar dem.
2. För att ta bort tomma kolumner, använd [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankcolumns/)-metoden.

{{% /alert %}}

## C++ kod för att ta bort tomma rader

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an existing Excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";
    Workbook workbook(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = workbook.GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the Blank Rows from the worksheet
    sheet.GetCells().DeleteBlankRows();

    // Save the Excel file
    U16String outputFilePath = outDir + u"mybook.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Blank rows deleted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## C++ kod för att ta bort tomma kolumner

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";

    // Create a smart pointer to a new Workbook instance
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = wb->GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the blank columns from the worksheet
    sheet.GetCells().DeleteBlankColumns();

    // Save the excel file
    U16String outputFilePath = srcDir + u"mybook.out.xlsx";
    wb->Save(outputFilePath);

    std::cout << "Blank columns deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
