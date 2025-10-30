---
title: Ta bort PivotTabell från ett Kalkylblad med C++
linktitle: Ta bort PivotTabell
type: docs
weight: 60
url: /sv/cpp/delete-pivot-table-from-a-worksheet/
description: C++ kod för att ta bort PivotTabell för Excel Ark
keywords: c++ ta bort pivot tabell från kalkylblad, c++ ta bort pivot tabell från excel, hur man raderar pivot tabell med c++, ta bort pivot tabell med c++, ta bort pivot tabell från excel med c++, c++ radera pivot tabell, c++ ta bort pivot tabell, ta bort pivot tabell, radera pivot tabell, hur man tar bort pivot tabell
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller en funktion för att radera eller ta bort pivottabell från ett arbetsblad. Du kan ta bort pivottabellen med hjälp av pivottabellobjektet eller pivottabellens position. Använd [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) -metoden för att ta bort pivottabellen med hjälp av pivottabellobjektet och [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) metoden för att ta bort pivottabellen med hjälp av dess position i pivottabellssamlingen.

{{% /alert %}}

Följande kod tar bort två pivot-tabeller från kalkylbladet. Först tas pivot-tabellen bort med [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/)-metoden och sedan tas en till bort med [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/)-metoden.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object from source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table object
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Remove pivot table using pivot table object
    worksheet.GetPivotTables().Remove(pivotTable);

    // OR you can remove pivot table using pivot table position by uncommenting below line
    // worksheet.GetPivotTables().RemoveAt(0);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Pivot table removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
