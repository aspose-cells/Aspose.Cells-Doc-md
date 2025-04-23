---
title: Sätt pivottabellalternativ – Visa för tomma celler med C++
linktitle: Inställning av pivottabellalternativ  För tomma celler Visa
type: docs
weight: 40
url: /sv/cpp/setting-pivot-table-option-for-empty-cells-show/
description: Lär dig hur du ställer in "För tomma celler visa" alternativet i pivottabeller med Aspose.Cells i C++.
---

{{% alert color="primary" %}}

Du kan ställa in olika pivottabellalternativ med hjälp av Aspose.Cells. Ett sådant alternativ är "För tomma celler Visa". Genom att ställa in detta alternativ visas alla tomma celler i en pivottabell som en angiven sträng.

{{% /alert %}}

## **Inställning av pivottabellalternativ i Microsoft Excel**

För att hitta och ställa in detta alternativ i Microsoft Excel:

1. Välj en pivottabell och högerklicka.
1. Välj **Pivottabellalternativ**.
1. Välj fliken **Layout & Format**.
1. Välj alternativet **Visa en sträng för tomma celler** och ange en sträng.

## **Konfigurera Pivot Table Option med Aspose.Cells**

Aspose.Cells tillhandahåller egenskaperna [**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getdisplaynullstring/) och [**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/) för att ange pivot-tabellalternativet "Visa en sträng för tomma celler".

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Get the first pivot table
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    PivotTable pt = pivotTables.Get(0);

    // Indicating if or not display the empty cell value
    pt.SetDisplayNullString(true);

    // Indicating the null string
    pt.SetNullString(u"null");

    // Calculate pivot table data
    pt.CalculateData();

    // Set refresh data on opening file to false
    pt.SetRefreshDataOnOpeningFile(false);

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Relaterade artiklar

- [Formatering av Pivottabell](/cells/sv/cpp/formatting-pivot-table/)
