---
title: Option für Pivot Tabelle einstellen  "Für leere Zellen anzeigen" mit C++
linktitle: Pivot Tabellen Option einstellen – Leere Zellen anzeigen
type: docs
weight: 40
url: /de/cpp/setting-pivot-table-option-for-empty-cells-show/
description: Erfahren Sie, wie Sie die Option "Für leere Zellen anzeigen" in Pivot Tabellen mit Aspose.Cells und C++ einstellen.
---

{{% alert color="primary" %}}

Sie können verschiedene Pivot-Tabellen-Optionen mit Aspose.Cells einstellen. Eine Option ist "Leere Zellen anzeigen". Durch Festlegen dieser Option werden alle leeren Zellen in einer Pivot-Tabelle als bestimmter Text angezeigt.

{{% /alert %}}

## **Pivot-Tabellen-Option in Microsoft Excel einstellen**

Um diese Option in Microsoft Excel zu finden und einzustellen:

1. Wählen Sie eine Pivot-Tabelle aus und klicken Sie mit der rechten Maustaste.
1. Wählen Sie **PivotTable-Optionen** aus.
1. Wählen Sie das Registerkarte **Layout & Format** aus.
1. Wählen Sie die Option **Leere Zellen anzeigen** aus und geben Sie einen Text an.

## **Pivot-Tabellen-Option mit Aspose.Cells einstellen**

Aspose.Cells bietet die Eigenschaften [**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getdisplaynullstring/) und [**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/) zum Einstellen der Pivot-Tabellen-Option "Leere Zellen anzeigen".

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

## Verwandte Artikel

- [Pivot-Tabelle formatieren](/cells/de/cpp/formatting-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
