---
title: Pivot Tabelle aus einem Arbeitsblatt mit C++ löschen
linktitle: Pivot Tabelle löschen
type: docs
weight: 60
url: /de/cpp/delete-pivot-table-from-a-worksheet/
description: C++ Code zum Entfernen von PivotTabellen in Excel Arbeitsblättern mit Aspose.Cells.
keywords: c++ pivot tabelle aus arbeitsblatt entfernen, c++ pivot tabelle löschen, wie man pivot tabelle mit c++ löscht, pivot tabelle mit c++ entfernen, c++ pivot tabelle löschen, c++ pivot tabelle entfernen, pivot tabelle entfernen, pivot tabelle löschen, wie man pivot tabelle löscht
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Möglichkeit, eine Pivot-Tabelle aus einem Arbeitsblatt zu löschen oder zu entfernen. Sie können die Pivot-Tabelle unter Verwendung des Pivot-Tabelle-Objekts oder der Position der Pivot-Tabelle löschen. Bitte verwenden Sie die [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/)-Methode, um die Pivot-Tabelle unter Verwendung des Pivot-Tabelle-Objekts zu löschen, und die [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/)-Methode, um das Pivot-Tabellen-Objekt unter Verwendung seiner Position innerhalb der Pivot-Tabellensammlung zu löschen.

{{% /alert %}}

Der folgende Beispielcode löscht zwei Pivot-Tabellen aus dem Arbeitsblatt. Zuerst wird die Pivot-Tabelle mit [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) Methode entfernt, dann mit [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/).

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
